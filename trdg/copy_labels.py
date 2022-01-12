import os
from tqdm import tqdm
import subprocess

process = subprocess.check_output(["python", "len_files.py", "out"])
length = int(process)

train_split = 0.9 * length
val_split = 0.8 * (length - train_split)



def copy_labels():
    with open('all_data/labels.txt', 'r', encoding='utf8') as f:
        l = f.readlines()

    tr = l[:train_split]
    val = l[train_split:val_split]
    test = l[val_split:]

    with open('all_data/train/labels.txt', 'a') as f:
        f.writelines(tr)

    with open('all_data/val/labels.txt', 'a') as f:
        f.writelines(val)

    with open('all_data/test/labels.txt', 'a') as f:
        f.writelines(test)

def main():
    copy_labels()


if __name__ == '__main__':
    main()
