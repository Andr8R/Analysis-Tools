#!/bin/bash
#SBATCH --account=def-pdeperio
#SBATCH --mem=1G               # memory (per node)
#SBATCH --time=0-1:10            # time (DD-HH:MM)
#SBATCH --cpus-per-task=4 

module load scipy-stack/2020b
python make_split_idxs_path.py
