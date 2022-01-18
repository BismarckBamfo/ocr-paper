import os
from fire import Fire


def len_files(src):
    '''
    This function returns the number of files in a directory.
    
    :param src: the directory where the files are located
    :return: The number of files in the directory.
    '''
    return len(os.listdir(f'{src}'))


def main():
    Fire(len_files)


if __name__ == '__main__':
    main()
