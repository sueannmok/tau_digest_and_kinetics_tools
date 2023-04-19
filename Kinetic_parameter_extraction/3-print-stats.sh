#! /bin/bash
# Olivier Julien, 2014
# ----------------------------
./1-fit-all.sh > temp.txt
cat temp.txt | egrep -B 18 Theil | egrep -v "Theil|Fitting|Initial|Tolerance|Relative|Computed|Chi-square|Correlation|RMS" | egrep -v "a0 = 0$|a1 = 1000$|a2 = 10$|a3 = 2$"
cat temp.txt | egrep -B 18 Theil | egrep -v "Theil|Fitting|Initial|Tolerance|Relative|Computed|Chi-square|Correlation|RMS" | egrep -v "a0 = 0$|a1 = 1000$|a2 = 10$|a3 = 2$" > log.txt
\rm temp.txt
