#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 15:56:39 2022

@author: kerry
"""
import Bio.SeqUtils as bio
import csv

#Since we are only looking at tau I created a dictionary for the 6 isform sequences. In future versions we could append tag sequences etc but I think this is functional for now.
"""dictionary for isoform sequences"""
isodict = {"0N3R":"MAEPRQEFEVMEDHAGTYGLGDRKDQGGYTMHQDQEGDTDAGLKAEEAGIGDTPSLEDEAAGHVTQARMVSKSKDGTGSDDKKAKGADGKTKIATPRGAAPPGQKGQANATRIPAKTPPAPKTPPSSGEPPKSGDRSGYSSPGSPGTPGSRSRTPSLPTPPTREPKKVAVVRTPPKSPSSAKSRLQTAPVPMPDLKNVKSKIGSTENLKHQPGGGKVQIVYKPVDLSKVTSKCGSLGNIHHKPGGGQVEVKSEKLDFKDRVQSKIGSLDNITHVPGGGNKKIETHKLTFRENAKAKTDHGAEIVYKSPVVSGDTSPRHLSNVSSTGSIDMVDSPQLATLADEVSASLAKQGL", "0N4R":"MAEPRQEFEVMEDHAGTYGLGDRKDQGGYTMHQDQEGDTDAGLKAEEAGIGDTPSLEDEAAGHVTQARMVSKSKDGTGSDDKKAKGADGKTKIATPRGAAPPGQKGQANATRIPAKTPPAPKTPPSSGEPPKSGDRSGYSSPGSPGTPGSRSRTPSLPTPPTREPKKVAVVRTPPKSPSSAKSRLQTAPVPMPDLKNVKSKIGSTENLKHQPGGGKVQIINKKLDLSNVQSKCGSKDNIKHVPGGGSVQIVYKPVDLSKVTSKCGSLGNIHHKPGGGQVEVKSEKLDFKDRVQSKIGSLDNITHVPGGGNKKIETHKLTFRENAKAKTDHGAEIVYKSPVVSGDTSPRHLSNVSSTGSIDMVDSPQLATLADEVSASLAKQGL", "1N3R":"MAEPRQEFEVMEDHAGTYGLGDRKDQGGYTMHQDQEGDTDAGLKESPLQTPTEDGSEEPGSETSDAKSTPTAEAEEAGIGDTPSLEDEAAGHVTQARMVSKSKDGTGSDDKKAKGADGKTKIATPRGAAPPGQKGQANATRIPAKTPPAPKTPPSSGEPPKSGDRSGYSSPGSPGTPGSRSRTPSLPTPPTREPKKVAVVRTPPKSPSSAKSRLQTAPVPMPDLKNVKSKIGSTENLKHQPGGGKVQIVYKPVDLSKVTSKCGSLGNIHHKPGGGQVEVKSEKLDFKDRVQSKIGSLDNITHVPGGGNKKIETHKLTFRENAKAKTDHGAEIVYKSPVVSGDTSPRHLSNVSSTGSIDMVDSPQLATLADEVSASLAKQGL","1N4R":"MAEPRQEFEVMEDHAGTYGLGDRKDQGGYTMHQDQEGDTDAGLKESPLQTPTEDGSEEPGSETSDAKSTPTAEAEEAGIGDTPSLEDEAAGHVTQARMVSKSKDGTGSDDKKAKGADGKTKIATPRGAAPPGQKGQANATRIPAKTPPAPKTPPSSGEPPKSGDRSGYSSPGSPGTPGSRSRTPSLPTPPTREPKKVAVVRTPPKSPSSAKSRLQTAPVPMPDLKNVKSKIGSTENLKHQPGGGKVQIINKKLDLSNVQSKCGSKDNIKHVPGGGSVQIVYKPVDLSKVTSKCGSLGNIHHKPGGGQVEVKSEKLDFKDRVQSKIGSLDNITHVPGGGNKKIETHKLTFRENAKAKTDHGAEIVYKSPVVSGDTSPRHLSNVSSTGSIDMVDSPQLATLADEVSASLAKQGL", "2N3R":"MAEPRQEFEVMEDHAGTYGLGDRKDQGGYTMHQDQEGDTDAGLKESPLQTPTEDGSEEPGSETSDAKSTPTAEDVTAPLVDEGAPGKQAAAQPHTEIPEGTTAEEAGIGDTPSLEDEAAGHVTQARMVSKSKDGTGSDDKKAKGADGKTKIATPRGAAPPGQKGQANATRIPAKTPPAPKTPPSSGEPPKSGDRSGYSSPGSPGTPGSRSRTPSLPTPPTREPKKVAVVRTPPKSPSSAKSRLQTAPVPMPDLKNVKSKIGSTENLKHQPGGGKVQIVYKPVDLSKVTSKCGSLGNIHHKPGGGQVEVKSEKLDFKDRVQSKIGSLDNITHVPGGGNKKIETHKLTFRENAKAKTDHGAEIVYKSPVVSGDTSPRHLSNVSSTGSIDMVDSPQLATLADEVSASLAKQGL", "2N4R":"MAEPRQEFEVMEDHAGTYGLGDRKDQGGYTMHQDQEGDTDAGLKESPLQTPTEDGSEEPGSETSDAKSTPTAEDVTAPLVDEGAPGKQAAAQPHTEIPEGTTAEEAGIGDTPSLEDEAAGHVTQARMVSKSKDGTGSDDKKAKGADGKTKIATPRGAAPPGQKGQANATRIPAKTPPAPKTPPSSGEPPKSGDRSGYSSPGSPGTPGSRSRTPSLPTPPTREPKKVAVVRTPPKSPSSAKSRLQTAPVPMPDLKNVKSKIGSTENLKHQPGGGKVQIINKKLDLSNVQSKCGSKDNIKHVPGGGSVQIVYKPVDLSKVTSKCGSLGNIHHKPGGGQVEVKSEKLDFKDRVQSKIGSLDNITHVPGGGNKKIETHKLTFRENAKAKTDHGAEIVYKSPVVSGDTSPRHLSNVSSTGSIDMVDSPQLATLADEVSASLAKQGL"}

"""input asking for tau isoform used"""
isoform = input("What isoform are you mapping (0N3R,0N4R,1N3R,1N4R,2N3R,2N4R)?")


def Isosequence(isoform):
    """creating the query sequence"""
    global Sequence
    Sequence =""
    for key, value in isodict.items():
        if isoform == key:
         Sequence = Sequence + value
         print("output:" + Sequence)
       
     
     
def band_list():
    """creating the band size list we are trying to match to sequence"""
    global bands
    bands = []
    global bandname
    bandname =""
    finish = False
    while finish == False:
        band_input = input("What kDa are your bands (one size at a time) Type END to finish: ")
        if band_input != "END":
            bands.append(band_input)
            bandname =bandname + str(band_input) + "_"
        elif band_input == "END":
            finish = True
    return bands


#added dictionary for isoforms to deal with numbering
isonumber_dict = {"0N3R": [58,31,45,275], "0N4R": [58,0,45,275], "1N3R": [29,31,74,275], "1N4R":[29,0,74,275], "2N3R": [0,31,103,275], "2N4R":[0,0,103,275]} 

def isoadjust(isoform):
    """creating a list to adjust the numbering to conventional 2N4R isform numbering system"""
    global isoad
    isoad=[]
    for key, value in isonumber_dict.items():
        if isoform == key:
         isoad = isoad + value
         #print("test" + str(isoad)) 
         #isoad=list(map(int, isoad))
    return isoad     
    
         
   #added statement to deal with isoform numbering of bands 
def Ab_list(isoad):
    """defining the antibody range used to check sequence that takes into account isoform choice"""
    global Ab_upper
    global Ab_lower
    Ab_upper = []
    Ab_lower = []
    global abname
    abname = ""
    finish = False
    while finish == False:
        Ab_input = input("What antibodies are your fragments reactive eg. ET3, 77G7, DA9? Type END to finish: ")
        if Ab_input == "END":
            finish = True
        if Ab_input == "ET3" and isoad[1] ==0:
            Ab_upper.append(288-isoad[0])
            Ab_lower.append(273-isoad[0])
            abname=abname+"ET3_"
        elif Ab_input == "ET3" and isoad[1] ==31:
            print("error: 3R isoforms are not detected by ET3 antibody")
        elif Ab_input == "77G7":
            Ab_upper.append(355-isoad[0]-isoad[1])
            Ab_lower.append(316-isoad[0]-isoad[1])
            abname=abname+"77G7_"
        elif Ab_input == "DA9":
            Ab_upper.append(140-isoad[0])
            Ab_lower.append(102-isoad[0])
            abname=abname+"DA9_"
    return Ab_upper
    return Ab_lower
            
        
#Added statement to deal with no trypsin cutting if P1'=proline with two exceptions

def peptide_scan(Seq):
    """checks for trypsin cut site and if found runs the peptide fragment function"""
    band_list()
    Ab_list(isoad)
    global i  
    i = 0
    create_output()
    while i < len(Seq):
        if Seq[i] == "K" or Seq[i] == "R" and Seq[i+1] != "P":
            peptide_fragment(Sequence, i, bands, Ab_upper, Ab_lower)
            i += 1
        elif Seq[i-1:i+1] =="WKP" or Seq[i-1:i+1] =="MRP":
            peptide_fragment(Sequence, i, bands, Ab_upper, Ab_lower)
            i += 1
        else:
            i += 1 

def peptide_fragment(Seq, i, bands, Ab_u, Ab_l):
    """creates the peptide fragment and matches to size and antibody detection"""
    i2 = i
    while i2 < len(Seq):
        if Seq[i2] == "K" or Seq[i2] =="R":
            frag = Seq[i:i2+1]
            weight = bio.molecular_weight(frag, seq_type="protein", double_stranded=(False),circular=False,monoisotopic=False)
            if (weight/1000) >= 1:
                for band in bands:
                    if abs(int(band) - weight/1000) <= 1:
                        index = 0
                        while index < len(Ab_lower):
                            if i <= Ab_lower[index] and i2 >= Ab_upper[index]:
                                index += 1
                            else:
                                break
                        if index == len(Ab_lower):
                            write_result(i, i2, frag, weight/1000)
                i2 += 1
            else:
                i2 += 1
        else: 
            i2 += 1


        
def create_output():
    """creates csv with possible band fragment information"""
    global csv_name
    csv_name =bandname +"_"+abname+ ".csv"
    csv_name = csv_name.strip()
    
    with open(csv_name,'w') as f:
        thewriter=csv.writer(f)
        thewriter.writerow(["Cut_site_locations", "Cut_site_locations_2N4R_numbering", "Peptide_fragment_sequence", "MW"])

def finalnumbers(i,i2):
    """adjusting numbering for fragments in output file to match 2N4R numbering"""
    i=i+1
    i2=i2+1
    global name2
    name2=""
    if i < isoad[2] and i2 < isoad[2]:
        name2=str(i) + " to " + str(i2)
    elif i < isoad[2] and i2 >= isoad[2]:
        name2=str(i) + " to " + str(i2+isoad[0])
    elif i in range(isoad[2],isoad[3]) and i2<isoad[3]:
        name2=str(i + isoad[0]) + " to " + str(i2 + isoad[0])
    elif i in range(isoad[2],isoad[3])and i2 >= isoad[3]:
        name2=str(i + isoad[0]) + " to " + str(i2 + isoad[0] + isoad[1])
    elif i >= isoad[3]:
        name2=str(i + isoad[0] + isoad[1]) + " to " + str(i2 + isoad[0] +isoad[1])
    else:
        name2="error in adjusting number range"
    return name2   
 
def write_result(i, i2, pep, MW): 
    """write info for each potential fragment"""
    name = str(i + 1) + " to " + str(i2 + 1)
    finalnumbers(i,i2)
    tmp2 =[]
    tmp2.append(name)
    tmp2.append(name2)
    tmp2.append(pep)
    tmp2.append(MW)
    with open(csv_name,'a+',newline='') as f:
        thewriter=csv.writer(f)
        thewriter.writerow(tmp2)

Isosequence(isoform)
isoadjust(isoform)     
peptide_scan(Sequence)
print("filename output:" + csv_name)

