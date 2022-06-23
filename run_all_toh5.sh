#!/bin/bash
#SBATCH --account=def-pdeperio
#SBATCH --mem=20G               # memory (per node)
#SBATCH --time=2-12:00            # time (DD-HH:MM)
#SBATCH --cpus-per-task=1

python convert_npz_to_h5.py
