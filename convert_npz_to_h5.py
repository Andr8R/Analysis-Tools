import os
import logging
from utils import check_output_path, set_logging
import argparse

def process_multi_npz(data_dir):
    log_pth = os.path.join(data_dir, "../../logs", "log_npz_to_h5.log")
    check_output_path(log_pth)
    set_logging(log_pth)
    total_count = 0
    for part in range(1, 8):
        part = str(part)
        log_text = f"Processing part {part} in {data_dir} \n"
        print(log_text), logging.info(log_text)

        npz_dir = data_dir
        h5_dir = os.path.join(data_dir, "../h5data/")
        check_output_path(h5_dir)

        for npz_file in os.listdir(npz_dir):
            if '.npz' in npz_file:
                npz_pth = os.path.join(npz_dir, npz_file)
                basename = os.path.basename(npz_file)
                basename = os.path.splitext(basename)[0]
                h5_pth = os.path.join(h5_dir, basename+'.h5')
                total_count += 1
                log_text = f"{total_count}: {npz_file}"
                print(log_text), logging.info(log_text)
                os.system(
                        f'sbatch --time=1:20:0 --job-name=npztoh5.{total_count} \
                        make_digihit_h5.sh {npz_pth} -o {h5_pth}'
                )

            # if total_count > 1:
            #     break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, default = 'test_run/4/npzdata')   
    args = parser.parse_args()
    print(args)

    process_multi_npz(data_dir = args.data_dir)



