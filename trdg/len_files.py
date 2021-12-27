import os
from fire import Fire


def len_files(src):
   return len(os.listdir(f'{src}'))


def main():
    Fire(len_files)


if __name__ == '__main__':
    main()
