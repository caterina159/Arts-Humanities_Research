#!/usr/bin/bash
#this may be changed to /bin/bash
parallel -j 2 ./files.sh {} ::: `seq 1551 1769` 
