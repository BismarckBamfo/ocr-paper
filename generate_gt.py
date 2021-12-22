import os
import re
from fire import Fire
import multiprocessing as Pool

def generate_gt(path):
    if path.endswith('/'):
        path = path.rstrip('/')
    p = os.listdir(path)
    names = []
    print('-----------')
    print('STARTING')
    print('-----------')
    for i, x in enumerate(p):
        idx = [i.start() for i in re.finditer('_', x)]
        idx = idx[-1]
        label = x[:idx]
        src = f'{path}/{x}'
        target = f'{path}/word_{i}.jpg'
        os.rename(src, target)
        t = f'word_{i}.jpg\t{label}\n'
        names.append(t)

    print('-----------')
    print('SAVING FILE')
    print('-----------')
    with open(f'{path}/gt.txt', 'w') as f:
        f.writelines(names)


if __name__ == '__main__':
    Fire(generate_gt)
