import os
import time
import string
import yaml

import torch
import torch.backends.cudnn as cudnn
import torch.utils.data
import torch.nn.functional as F
import numpy as np
from nltk.metrics.distance import edit_distance

from utils import CTCLabelConverter, AttnLabelConverter, Averager, AttrDict
from dataset import hierarchical_dataset, AlignCollate
from arch.tw import Model

cudnn.benchmark = True
cudnn.deterministic = False

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')



def demo(opt):
    """ model configuration """
    if 'CTC' in opt.Prediction:
        converter = CTCLabelConverter(opt.character_list)
    else:
        converter = AttnLabelConverter(opt.character_list)
    num_class = len(converter.character)

    if opt.rgb:
        opt.input_channel = 3
    model = Model(num_class=num_class, **opt.network_params, opt=opt)
    '''print('model input parameters', opt.imgH, opt.imgW, opt.num_fiducial, opt.input_channel, opt.output_channel,
          opt.hidden_size, opt.num_class, opt.batch_max_length, opt.Transformation, opt.FeatureExtraction,
          opt.SequenceModeling, opt.Prediction)
    '''
    model = torch.nn.DataParallel(model).to(device)

    # load model
    print('loading pretrained model from %s' % opt.saved_model)
    model.load_state_dict(torch.load(opt.saved_model, map_location=device))

    # prepare data. two demo images from https://github.com/bgshih/crnn#run-demo
    AlignCollate_test = AlignCollate(imgH=opt.imgH, imgW=opt.imgW, keep_ratio_with_pad=opt.PAD, contrast_adjust=opt.contrast_adjust)
    demo_dataset, demo_dataset_log, length = hierarchical_dataset(root=opt.test_data, opt=opt)
    demo_loader = torch.utils.data.DataLoader(
        demo_dataset, batch_size=min(32, opt.batch_size),
        shuffle=False,  # 'True' to check training progress with validation function.
        num_workers=int(opt.workers), prefetch_factor=512,
        collate_fn=AlignCollate_test, pin_memory=True)
    
    # predict
    model.eval()
    with torch.no_grad():
        for image_tensors, image_path_list in demo_loader:
            batch_size = image_tensors.size(0)
            image = image_tensors.to(device)
            # For max length prediction
            length_for_pred = torch.IntTensor([opt.batch_max_length] * batch_size).to(device)
            text_for_pred = torch.LongTensor(batch_size, opt.batch_max_length + 1).fill_(0).to(device)

            if 'CTC' in opt.Prediction:
                preds = model(image, text_for_pred)
                # Select max probabilty (greedy decoding) then decode index to character
                preds_size = torch.IntTensor([preds.size(1)] * batch_size)

                if opt.decode == 'greedy':
                    # Select max probabilty (greedy decoding) then decode index to character
                    _, preds_index = preds.max(2)
                    preds_index = preds_index.view(-1)
                   
                    preds_str = converter.decode_greedy(preds_index.data.cpu().detach().numpy(), preds_size.data)
                elif opt.decode == 'beamsearch':
                    preds_str = converter.decode_beamsearch(preds, beamWidth=2)

            else:
                preds = model(image, text_for_pred, is_train=False)

                # select max probabilty (greedy decoding) then decode index to character
                _, preds_index = preds.max(2)
                preds_str = converter.decode(preds_index, length_for_pred)


            log = open(f'./log_demo_result.txt', 'a')
            dashed_line = '-' * 80
            head = f'{"image_path":25s}\t{"predicted_labels":25s}\tconfidence score'
            
            print(f'{dashed_line}\n{head}\n{dashed_line}')
            log.write(f'{dashed_line}\n{head}\n{dashed_line}\n')

            acc = 0

            preds_prob = F.softmax(preds, dim=2)
            preds_max_prob, _ = preds_prob.max(dim=2)
            for img_name, pred, pred_max_prob in zip(image_path_list, preds_str, preds_max_prob):
                if 'Attn' in opt.Prediction:
                    pred_EOS = pred.find('[s]')
                    pred = pred[:pred_EOS]  # prune after "end of sentence" token ([s])
                    pred_max_prob = pred_max_prob[:pred_EOS]

                # calculate confidence score (= multiply of pred_max_prob)
                confidence_score = pred_max_prob.cumprod(dim=0)[-1]
                if img_name == pred:
                    acc += 1
                print(f'{img_name:25s}\t{pred:25s}\t{confidence_score:0.4f}')
                log.write(f'{img_name:25s}\t{pred:25s}\t{confidence_score:0.4f}\n')
            accuracy = (acc / length) * 100
        log.write(f'Accuracy = {accuracy}')
        log.close()


if __name__ == '__main__':
    
    file_path = 'arch/tw.yaml'
    with open(file_path, 'r', encoding="utf8") as stream:
        opt = yaml.safe_load(stream)
    opt = AttrDict(opt)

    cudnn.benchmark = True
    cudnn.deterministic = True
    opt.num_gpu = torch.cuda.device_count()

    demo(opt)