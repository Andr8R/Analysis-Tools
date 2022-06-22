import os
import logging
from utils import check_output_path, set_logging
import argparse

def process_multi_wcsim(output_dir = './output/', data_dir = '/project/rpp-blairt2k/jwalker/iwcd/production_20200106/'):
    log_pth = os.path.join(output_dir, "logs", "log_wcsim_to_npz.log")
    check_output_path(log_pth)
    set_logging(log_pth)
    total_count = 0
    for part in range(1, 8):
        part = str(part)
        log_text = f"Processing part {part} in {data_dir} \n"
        print(log_text), logging.info(log_text)

        wcsim_dir = os.path.join(data_dir, "WCSim/fhc/", part)
        fitqun_dir = os.path.join(data_dir, "fiTQun/fhc/", part)
        out_npz = os.path.join(output_dir, part, "npzdata")
        out_fitqun = os.path.join(output_dir, part, "fitqun")
        check_output_path(out_npz)
        check_output_path(out_fitqun)

        for wcsim_file in os.listdir(wcsim_dir):
            fitqun_file = wcsim_file.replace("wcsim", "fitqun")
            wcsim_pth = os.path.join(wcsim_dir, wcsim_file)
            fitqun_pth = os.path.join(fitqun_dir, fitqun_file)
            if not 'flat' in wcsim_file:
                total_count += 1
                log_text = f"{total_count}: {wcsim_file}"
                print(log_text), logging.info(log_text)
                os.system(
                        f'sbatch --job-name=wcsimtonpz.{total_count} make_npz.sh {wcsim_pth} {out_npz}'
                )

                os.system(
                        f'scp {fitqun_pth} {out_fitqun}'
                )
            # if total_count > 1:
            #     break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, default = '/project/rpp-blairt2k/jwalker/iwcd/production_20200106/')   
    parser.add_argument('--output-dir', type=str, default = './test_run/')   
    args = parser.parse_args()
    print(args)

    process_multi_wcsim(output_dir = args.output_dir, data_dir = args.data_dir)



