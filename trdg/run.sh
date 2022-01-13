#!/bin/zsh
python run.py -c 116657 -l tw -na 2 -tc '#000000,#888888' -f 32 -k 15 -rk -bl 1 -rbl -b 0 -t 5 --output_dir dataset_1
python run.py -c 116657 -l tw -na 2 -tc '#000000,#888888' -f 32 -k 15 -rk -bl 1 -rbl -b 1 -t 5 --output_dir dataset_2
python run.py -c 116657 -l tw -na 2 -tc '#000000,#888888' -f 32 -k 15 -rk -bl 1 -rbl -b 2 -t 5 --output_dir dataset_3
python run.py -c 116657 -l tw -na 2 -tc '#000000,#888888' -f 32 -k 15 -rk -bl 1 -rbl -b 3 -t 5 --output_dir dataset_4
mkdir dataset_copies
mkdir out
mkdir all_data
mkdir all_data/train
mkdir 'all_data/test'
mkdir all_data/val
cp -r dataset_1 dataset_2 dataset_3 dataset_4 dataset_copies
python offset_datasets.py dataset_1 dataset_2 dataset_3 dataset_4
python combine_labels.py dataset_1 dataset_2 dataset_3 dataset_4
python copy_folder_contents.py dataset_1 dataset_2 dataset_3 dataset_4 out
python copy_labels.py
python copy_files.py
python labels_csv.py all_data
rm all_data/labels.txt
rm all_data/train/labels.txt
rm all_data/val/labels.txt
rm 'all_data/test/labels.txt'
