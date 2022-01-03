import os


def copy_labels():
    with open('all_data/labels.txt', 'r', encoding='utf8') as f:
        l = f.readlines()

    tr = l[:100000]
    val = l[100000:110000]
    test = l[110000:116657]

    with open('all_data/labels_train.txt', 'a') as f:
        f.writelines(tr)

    with open('all_data/labels_val.txt', 'a') as f:
        f.writelines(val)

    with open('all_data/labels_test.txt', 'a') as f:
        f.writelines(test)

def main():
    copy_labels()


if __name__ == '__main__':
    main()