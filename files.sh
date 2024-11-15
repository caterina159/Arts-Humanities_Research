#!/usr/bin/bash
#create the files for the python script
year=$1
python3 network_python.py --birth_year $year --gender male > out_$year

