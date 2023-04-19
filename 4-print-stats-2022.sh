#! /bin/bash
# Olivier Julien, 2014
# ----------------------------
./1-fit-all.sh > temp.txt
cat temp.txt | egrep -B 18 Theil | egrep -v "Theil|Fitting|Initial|Tolerance|Relative|Computed"
cat temp.txt | egrep -B 18 Theil | egrep -v "Theil|Fitting|Initial|Tolerance|Relative|Computed" > log.txt
\rm temp.txt
