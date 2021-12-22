import re
import os
from typing import List
import argparse


class DataLoader:
    def __init__(self, opt):
        self._input_path = opt.input_path
        self._output_filename = os.path.join(opt.output_dir, opt.output_filename)

    def read(self):
        self._texts = ''
        for filename in os.listdir(self._input_path):
            if os.path.isfile(filename):
                print(f'Reading file {filename}')
                with open(filename, 'r', 'utf-8') as f:
                    self._data = f.read()
                    print(f'Appending file {filename}')
                self._texts += self._data

            else:
                continue
        '''
        else:
            print("Reading file {self._input_filenames}")
            with open(self._input_filenames, "r") as f:
                self._data = f.read()
                print("Appending file {self._input_filenames}")
            self._texts += self._data

        return self._texts
        '''
    def output(self):
        print(self._texts)


class DataCleaner(DataLoader):
    def __init__(self, opt):
        super(DataCleaner, self).__init__(opt)

    def __len__(self) -> int:
        return len(self)

    def reader(self) -> str:
        return self.read()

    def clean(self) -> set:
        print("Cleaning started...")
        self._x = re.split("\s", self.reader())
        self._x = [data for data in self._x if data != '']
        self._x = set(self._x)
        print("Cleaning finished!")
        return self._x

    def tokenize(self) -> set:
        return self.clean()

    def save(self):
        try:
            os.makedirs(opt.output_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        print(f"Saving file as {self._output_filename}")
        with open(self._output_filename, 'w') as f:
            f.write('\n'.join(self._x))


def main():
    parser = argparse.ArgumentParser(description='Create unique tokens from a group of text')

    parser.add_argument(
            '--input_dir',
            type=str, help='Path to the dataset containing your text'
            )

    parser.add_argument(
            '--output_filename',
            type=str,
            help='Output filename'
            )

    parser.add_argument(
        "--output_dir",
        type=str,
        help="The output directory",
        default=f"{os.path.join(os.path.split(os.path.realpath(__file__))[0], 'out')}"
    )
    args = parser.parse_args()

    data = DataCleaner(args, input_path, output_filename)
    data.tokenize()
    data.save()


if __name__ == '__main__':
    main()

# python3 clean_data.py --input_path=
