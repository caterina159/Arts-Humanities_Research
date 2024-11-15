#!/bin/bash 
#loop to run the python script multiple times 
years=('1610' '1620' '1630' '1640' '1650' '1660' '1670' '1680' '1690' '1700') 
for year in ${years[@]} 
do 
        py network_python.py --birth_year $year --gender male 
        echo "Year per iteration:$year" 
        echo "---------------------" 
done 
