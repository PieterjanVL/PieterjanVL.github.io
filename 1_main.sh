#!/bin/bash 
set -o errexit   # abort on nonzero exitstatus
set -o nounset   # abort on unbound variable
set -o pipefail  # don't hide errors within pipes

DIR=/home/pieterjan/Documents/Hogent/22-23/Linux/Rapport
timestamp=$(date +%F_%T)
timestamp2=$(date +%F_%H-%M-%S)

echo "${timestamp}"
echo "${timestamp2}"

export DIR
export timestamp
export timestamp2
/home/pieterjan/Documents/Hogent/22-23/Linux/Rapport/2_setup.sh
/home/pieterjan/Documents/Hogent/22-23/Linux/Rapport/3_data_verzamelen.sh
/home/pieterjan/Documents/Hogent/22-23/Linux/Rapport/4_data_transformeren.sh
python3 /home/pieterjan/Documents/Hogent/22-23/Linux/Rapport/5_data_analyseren.py "${DIR}" "${timestamp2}"
python3 /home/pieterjan/Documents/Hogent/22-23/Linux/Rapport/6_raport_genereren.py "${DIR}" "${timestamp2}"
printf "* Rapport gemaakt op [%s](rapport/%s.md)\n" "${timestamp}" "${timestamp2}" | cat - README.md > temp && mv temp README.md
