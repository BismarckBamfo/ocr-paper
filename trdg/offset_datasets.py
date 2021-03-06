import os
import sys
import subprocess
'''
Combine datasets into one folder
python offset_datasets.py --path=<dataset_path>
'''
datasets = sys.argv[1:]
print(datasets)
def offset_datasets_and_labels():
    for dataset in datasets:
        if dataset.endswith('2'):
            offset = subprocess.check_output(["python", "len_files.py", "dataset_1"])
            offset = int(offset) - 1

        elif dataset.endswith('3'):
            offset = subprocess.check_output(["python", "len_files.py", "dataset_2"])
            offset = (int(offset) - 1) * 2

        elif dataset.endswith('4'):
            offset = subprocess.check_output(["python", "len_files.py", "dataset_3"])
            offset = (int(offset) - 1) * 3

        else:
            continue

        dirs = os.listdir(dataset)
        for dir_ in dirs:
            if dir_.endswith('.jpg'):
                new_file = dir_[0:-4]
                offset_filename = int(new_file) + offset
                src = f'{dataset}/{dir_}'
                target = f'{dataset}/{offset_filename}.jpg'
                os.rename(src, target)

        with open(f'{dataset}/labels.txt', 'r') as f:
            text = f.readlines()

        for idx ,x in enumerate(text):
            rename = x.split('\t')
            rename[0] = str(int(rename[0][:-4]) + offset) + '.jpg'
            rename = f'{rename[0]}\t{rename[1]}'
            text[idx] = rename

        with open(f'{dataset}/labels.txt', 'w') as f:
            f.writelines(text)


def main():
    offset_datasets_and_labels()

if __name__ == '__main__':
    main()

