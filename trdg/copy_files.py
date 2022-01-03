import os
import shutil

src = 'out/'

def copy_files_train(dest = 'all_data/train/'):
    for i in range(100000):
        sr = f'{src}{i}.jpg'
        tgt = f'{dest}{i}.jpg'
        shutil.move(sr, tgt)

def copy_files_val(dest = 'all_data/val/'):
    for i in range(100000, 110000):
        sr = f'{src}{i}.jpg'
        tgt = f'{dest}{i}.jpg'
        shutil.move(sr, tgt)

def copy_files_test(dest = 'all_data/test/'):
    for i in range(110000, 116657):
        sr = f'{src}{i}.jpg'
        tgt = f'{dest}{i}.jpg'
        shutil.move(sr, tgt)
    
    

if __name__ == '__main__':
    copy_files_train()
    copy_files_test()
    copy_files_val()
