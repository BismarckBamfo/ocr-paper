import pandas as pd
from fire import Fire

def make_train_csv(path):
    filename = []
    words = []
    with open(f'{path}/train/labels.txt', 'r') as f:
        train_text = f.readlines()
    for idx, x in enumerate(train_text):
        split_line = x.split('\t')
        filename.append(split_line[0])
        words.append(split_line[1].rstrip('\n').lstrip())

    df = pd.DataFrame(list(zip(filename, words)), columns=['filename', 'words'])
    df.to_csv(f'{path}/train/labels.csv', sep='\t', encoding='utf-8', index=False)


def make_val_csv(path):
    filename = []
    words = []
    with open(f'{path}/val/labels.txt', 'r') as f:
        train_text = f.readlines()

    for idx, x in enumerate(train_text):
        split_line = x.split('\t')
        filename.append(split_line[0])
        words.append(split_line[1].rstrip('\n').lstrip())

    df = pd.DataFrame(list(zip(filename, words)), columns=['filename', 'words'])
    df.to_csv(f'{path}/val/labels.csv', sep='\t', encoding='utf-8', index=False)


def make_test_csv(path):
    filename = []
    words = []
    with open(f'{path}/test/labels.txt', 'r') as f:
        train_text = f.readlines()

    for idx, x in enumerate(train_text):
        split_line = x.split('\t')
        filename.append(split_line[0])
        words.append(split_line[1].rstrip('\n').lstrip())

    df = pd.DataFrame(list(zip(filename, words)), columns=['filename', 'words'])
    df.to_csv(f'{path}/test/labels.csv', sep='\t', encoding='utf-8', index=False)


def main(path):
    make_train_csv(path)
    make_val_csv(path)
    make_test_csv(path)


if __name__ == '__main__':
    Fire(main)
