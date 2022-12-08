#!/bin/bash 
set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

DIR=$HOME/Documents/Rapport
timestamp=$(date +%F_%T)
timestamp2=$(date +%F_%H-%M-%S)

echo "${timestamp}"
echo "${timestamp2}"

export DIR
export timestamp
export timestamp2
$HOME/Documents/Rapport/2_setup.sh
$HOME/Documents/Rapport/3_data_verzamelen.sh
$HOME/Documents/Rapport/4_data_transformeren.sh
python3 $HOME/Documents/Rapport/5_data_analyseren.py "${DIR}" "${timestamp2}"
python3 $HOME/Documents/Rapport/6_raport_genereren.py "${DIR}" "${timestamp2}"
printf "* Rapport gemaakt op [%s](rapport/%s.md)\n" "${timestamp}" "${timestamp2}"  >> README.md
#./2_setup.sh 
#./3_data_verzamelen.sh #STAP 1
#./4_data_transformeren.sh #STAP 2