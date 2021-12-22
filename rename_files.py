import os
from fire import Fire


def rename(path):
    p = os.listdir(path)
    print('----------------')
    print('Starting Renaming')
    print('----------------')
    for x in p:
        filename = x[:-4]
        if 'c' in filename:
            filename = filename.replace('c', chr(8579)) if filename.index('c') == 0 else filename.replace('c', chr(8580))
        elif 'C' in filename:
            filename = filename.replace('C', chr(8580)) if filename.index('C') != 0 else filename.replace('C', chr(8579))
        if 'j' in filename:
            filename = filename.replace('j', chr(400)) if filename.index('j') == 0 else filename.replace('j', chr(949))
        if 'J' in filename:
            filename = filename.replace('J', chr(949)) if filename.index('J') != 0 else filename.replace('J', chr(400))
        src = f'{path}/{x}'
        target = f'{path}/{filename}.jpg'
        os.rename(src, target)
    print('----------------')
    print('Finished Renaming')
    print('----------------')


def main():
    Fire(rename)


if __name__ == '__main__':
    main()
