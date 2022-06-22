#!/bin/bash
#SBATCH --account=def-pdeperio
#SBATCH --mem=2G               # memory (per node)
#SBATCH --time=0-2:30            # time (DD-HH:MM)
#SBATCH --cpus-per-task=1 

echo "Sleeping for 30+-10 seconds to avoid hammering filesystems"
# sleep $((20 + RANDOM % 20))

DATATOOLS=./DataTools
source ${DATATOOLS}/cedar_scripts/sourceme.sh 
export WCSIMDIR=/project/rpp-blairt2k/machine_learning/production_software/WCSim_for_old_production

python ${DATATOOLS}/root_utils/event_dump.py $1 -d $2
echo $1