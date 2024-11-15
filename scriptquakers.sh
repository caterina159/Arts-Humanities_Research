#!/bin/bash
#SBATCH -N 1
#SBATCH -c 1
#SBATCH -t 00-00:03:33
#SBATCH -p cpu
#change output name for slurm job outputforloop.txt instead of slurm-number.out
#SBATCH -o outputforloop.txt
#SBATCH --qos=debug
#SBATCH --job-name=forloopQuakers
#create a sequence of files for each to receive the one line of output
source /home3/lxps38/test_env/bin/activate
for year in {1551..1769}
do
        filename=quakersfolder/quakers$year
        python network_python.py --birth_year $year --gender male > $filename
done
