import os
import shutil
import sys
from tqdm import trange
import subprocess
from math import ceil

src = 'out/'

process = subprocess.check_output(["python", "len_files.py", "out"])
length = int(process)

train_split = ceil(0.9 * length)
val_num = ceil(0.8 * (length - train_split))
val_split = train_split + val_num

'''
    These functions copies all the files from the source directory to the destination directory.
        The source directory is the directory where the images are stored.
        The destination directory is the directory where the images are copied to.
        The function is a for loop that iterates through the training split.
        The function uses the shutil.move function to move the files from the source to the destination.
        The function uses the tqdm function to create a progress bar.
    
    :param dest: the destination folder, defaults to all_data/<train or val or test/>/ (optional)
    :return: None
'''

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
    for i in trange(val_split, length):
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
