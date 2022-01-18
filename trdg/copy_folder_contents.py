import os
import shutil
import sys

def copy_files():
    '''
    Move all the files in the given directories to the target directory.
    
    
    :return: None
    '''
    src_directories = sys.argv[1:-1]
    tgt_directories = sys.argv[-1]
    for directory in src_directories:
        files = os.listdir(directory)
        for f in files:
            if f.endswith('.jpg') or f.endswith('.png'):
                src = f'{directory.rstrip("/")}/{f}'
                tgt = f'{tgt_directories.rstrip("/")}/{f}'
                shutil.move(src, tgt)

def main():
    copy_files()


if __name__ == '__main__':
    main()
