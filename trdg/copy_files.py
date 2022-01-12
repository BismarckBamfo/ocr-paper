import os
import shutil
import sys
from tqdm import trange
import subprocess

src = 'out/'

process = subprocess.check_output(["python", "len_files.py", "out"])
length = int(process)

train_split = 0.9 * length
val_split = 0.8 * (length - train_split)
test_split = length - train_split - val_split

def copy_files_train(dest = 'all_data/train/'):
    for i in trange(train_split):
        sr = f'{src}{i}.jpg'
        tgt = f'{dest}{i}.jpg'
        try:
            shutil.move(sr, tgt)
        except exception as e:
            pass
def copy_files_val(dest = 'all_data/val/'):
    for i in trange(train_split, val_split):
        sr = f'{src}{i}.jpg'
        tgt = f'{dest}{i}.jpg'
        try:
            shutil.move(sr, tgt)
        except exception as e:
            pass

def copy_files_test(dest = 'all_data/test/'):
    for i in trange(val_split, test_split):
        sr = f'{src}{i}.jpg'
        tgt = f'{dest}{i}.jpg'
        try:
            shutil.move(sr, tgt)
        except exception as e:
            pass

def main():
    copy_files_train()
    copy_files_test()
    copy_files_val()

if __name__ == '__main__':
    main()
