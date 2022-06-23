#!/bin/bash
#SBATCH --account=def-pdeperio
#SBATCH --mem=15G               # memory (per node)
#SBATCH --time=0-15:10            # time (DD-HH:MM)
#SBATCH --cpus-per-task=4 

python eval_files.py
