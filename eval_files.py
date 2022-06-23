import os
import logging
from utils import check_output_path, set_logging
import argparse

def process_multi_eval(data_dir, weights_pth, files_pth=None):
    log_pth = os.path.join(data_dir, "logs", "log_eval.log")
    check_output_path(log_pth)
    set_logging(log_pth)

    if files_pth is None:
        files_pth = os.path.join(data_dir, "files")

    total_count = 0
    for part in range(1, 8):
        h5_part = f'h5_files_{part}.txt'
        h5_files = os.path.join(files_pth, h5_part)
        for h5_file in open(h5_files, 'r').read().split('\n'):

            if total_count > 1:
                break

            h5_id, h5_dir = os.path.basename(h5_file), os.path.dirname(h5_file)
            split_id = 'split_'+h5_id.replace('.h5','.npz')
            split_dir = os.path.join(h5_dir, "../splitfiles/")
            split_pth = os.path.join(split_dir, split_id)
            dump_path = os.path.join('../../../', f'{h5_id}_')
            total_count += 1
            os.system(
                f'sbatch --job-name=eval{part}.{total_count} run_evaluate.sh {dump_path} {split_pth} {h5_file} {weights_pth}'
                )
            log_text = f"Processing part {part}: {h5_id} \n"
            print(log_text), logging.info(log_text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, default = 'test_run', help='parent data directory')   
    parser.add_argument('--files-dir', type=str, help='txt files location')   
    parser.add_argument('--weights', type=str, default = '../ClassifierBEST_long_07_04.pth')   
    args = parser.parse_args()
    print(args)

    process_multi_eval(data_dir = args.data_dir, files_pth = args.files_dir, weights_pth = args.weights)


