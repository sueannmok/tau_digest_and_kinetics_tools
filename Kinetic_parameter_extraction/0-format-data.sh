#! /bin/bash
#you will need to format a txt file with 1st column =time and subsequent columns as data (assay readings).Header should be in row 1. Type "last" in the header row of the first empty column after data.  The script is setup to analyze triplicate columns of data for a given group
#change filename for this script to match you formatted txt file
# ----------------------------

mkdir data
\rm data/*
./excel-to-single-files-no-gap.pl 2023117_familial_1stkinetics.txt
\rm data/last*
