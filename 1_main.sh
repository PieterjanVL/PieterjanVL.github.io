#!/bin/bash 
set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

DIR=$HOME/Documents/linux-22-23-PieterjanVL/data-workflow
timestamp=$(date +%F_%T)

export DIR
export timestamp
$HOME/Documents/linux-22-23-PieterjanVL/data-workflow/2_setup.sh
$HOME/Documents/linux-22-23-PieterjanVL/data-workflow/3_data_verzamelen.sh
$HOME/Documents/linux-22-23-PieterjanVL/data-workflow/4_data_transformeren.sh
python3 $HOME/Documents/linux-22-23-PieterjanVL/data-workflow/5_data_analyseren.py "${DIR}" "${timestamp}"
python3 $HOME/Documents/linux-22-23-PieterjanVL/data-workflow/6_raport_genereren.py "${DIR}" "${timestamp}"
#./2_setup.sh 
#./3_data_verzamelen.sh #STAP 1
#./4_data_transformeren.sh #STAP 2