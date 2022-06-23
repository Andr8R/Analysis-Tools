import os
import numpy as np
import h5py
import logging
from utils import check_output_path, set_logging
import argparse

def split_idxs(split_id, h5file):
  f = h5py.File(h5file, "r")
  idxs = np.arange(len(f['event_ids']))
  np.savez(split_id, test_idxs=idxs)

def process_splits(data_dir):
    log_pth = os.path.join(data_dir, "logs", "log_splits.log")
    files_pth = os.path.join(data_dir, "files")
    check_output_path(log_pth)
    check_output_path(files_pth)
    set_logging(log_pth)

    for part in range(1, 8):
        total_count = 0
        part = str(part)
        log_text = f"Processing part {part} in {data_dir} \n"
        print(log_text), logging.info(log_text)

        h5_dir = os.path.join(data_dir, part, "h5data/")
        # check_output_path(h5_dir)
        split_dir = os.path.join(data_dir, part, "splitfiles/")
        check_output_path(split_dir)
        fitqun_dir = os.path.join(data_dir, part, "fitqun/")


        fitqun_files = os.path.join(files_pth, "fitqun_files_"+part+".txt")
        h5_files = os.path.join(files_pth, "h5_files_"+part+".txt")
        file_fitqun = open(fitqun_files, "w")
        file_h5 = open(h5_files, "w")

        for path, subdirs, files in os.walk(h5_dir):
            for file_id in files:
                print(file_id), logging.info(file_id)
                h5_file_pth = os.path.join(path, file_id)
                fitqun_pth = os.path.join(fitqun_dir, file_id.replace("wcsim", "fitqun").replace('.h5', '.root'))
                split_id = 'split_'+file_id.replace('.h5','.npz')
                split_pth = os.path.join(split_dir, split_id)
                # if split_id not in os.listdir(split_dir):
                total_count += 1
                file_h5.write(str(h5_file_pth) + os.linesep)
                file_fitqun.write(str(fitqun_pth) + os.linesep)
                split_idxs(split_pth, h5_file_pth)
                
        log_text = f'In directory {part}, total: {total_count}'
        print(log_text), logging.info(log_text)
        file_fitqun.close()
        file_h5.close()   

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, default = 'test_run')   
    args = parser.parse_args()
    print(args)

    process_splits(data_dir = args.data_dir)
