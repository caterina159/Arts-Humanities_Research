#!/bin/bash
#SBATCH -N 1
#SBATCH -c 1
#SBATCH -t 00-00:00:10
#SBATCH -p cpu
#SBATCH --qos=debug
#SBATCH --job-name=forloopLessYears
source /home3/lxps38/test_env/bin/activate
years=('1610' '1620' '1630' '1640' '1650' '1660' '1670' '1680' '1690' '1700')
for year in ${years[@]}
do
        python network_python.py --birth_year $year --gender male
done
