#!/bin/bash
#SBATCH --account=def-pdeperio
#SBATCH --mem=20G               # memory (per node)
#SBATCH --time=3-15:10            # time (DD-HH:MM)
#SBATCH --cpus-per-task=6

python convert_wcsim_to_npz.py
