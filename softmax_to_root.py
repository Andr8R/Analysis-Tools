import numpy as np
import os
import uproot3 as uproot
import argparse

def check_output_path(output_path: str) -> str:
    if not os.path.exists(output_path):
        if not os.path.splitext(output_path)[1]:
            _out_dir = output_path
        else:
            _out_dir = os.path.dirname(output_path) 
        os.makedirs(_out_dir, exist_ok=True)

def convert(numpyfile, rootfile):
    softmax = np.load(numpyfile)
    g_array = softmax[:, 0]
    e_array = softmax[:, 1]
    mu_array = softmax[:, 2]

    with uproot.recreate(rootfile) as output:
        output['softmax_output'] = uproot.newtree({'prob_gamma': "float32", 'prob_e': "float32", 'prob_mu': "float32"})
        output['softmax_output'].extend({'prob_gamma': g_array, 'prob_e': e_array, 'prob_mu': mu_array})

def process_softmax_to_root(data_dir, files_pth=None):
    """
    data_dir: parent folder locally, contains 1,2,3,4,5,6,7,files dirs.
    """

    if files_pth is None:
        files_pth = os.path.join(data_dir, "files")

    total_count = 0
    for part in range(1, 8):
        fitqun_files = os.path.join(files_pth, f"fitqun_files_{part}.txt")
        softmax_files = os.path.join(files_pth, f"softmax_files_{part}.txt")
        file_softmax = open(softmax_files, "w")
        local_softmax_dir = f"{part}/softmax/"
        local_softmax_root_dir = f"{part}/softmax_root/"
        check_output_path(local_softmax_root_dir)
        
        for fitqun_file in open(fitqun_files, 'r').read().split('\n'):
            fitqun_id, fitqun_dir = os.path.basename(fitqun_file), os.path.dirname(fitqun_file)
            softmax_id = fitqun_id.replace("fitqun", "wcsim").replace('.h5', '_softmax.npy')
            softmax_root_id = fitqun_id.replace("fitqun", "softmax")
            # path of final softmax root file on cedar
            cedar_softmax_root_pth = os.path.join(fitqun_dir, "../softmax_root/", softmax_root_id)
            # local actions
            local_softmax_pth = os.path.join(local_softmax_dir, softmax_id)
            local_softmax_root_pth = os.path.join(local_softmax_root_dir, softmax_root_id)

            if softmax_id in os.listdir(local_softmax_dir):
                convert(local_softmax_pth, local_softmax_root_pth)
                total_count += 1
                softmax_files.write(str(cedar_softmax_root_pth) + os.linesep)
            else:
                print(f"missed {softmax_id}")
            
        softmax_files.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', type=str, default = 'test_run', help='parent data directory locally')   
    parser.add_argument('--files-dir', type=str, help='txt files location')   
    args = parser.parse_args()
    print(args)

    process_softmax_to_root(data_dir = args.data_dir, files_pth = args.files_dir)

