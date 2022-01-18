import os
import sys

'''
Combine labels to one lables.txt file and copy to all_data folder
python combine_labels.py path1, path2, path3
'''
def combine_labels():
    '''
    It combines the labels of the four datasets into one file.
    
    
    :return: None
    '''
    path1, path2, path3, path4 = sys.argv[1:]

    with open(f'{path1}/labels.txt') as f:
        text1 = f.readlines()


    with open(f'{path2}/labels.txt') as f:
        text2 = f.readlines()


    with open(f'{path3}/labels.txt') as f:
        text3 = f.readlines()

    with open(f'{path4}/labels.txt') as f:
        text4 = f.readlines()

    text1.extend(text2)
    text1.extend(text3)
    text1.extend(text4)


    with open(f'all_data/labels.txt', 'w', encoding='utf8') as f:
        f.writelines(text1)


def main():
    combine_labels()


if __name__ == '__main__':
    main()
