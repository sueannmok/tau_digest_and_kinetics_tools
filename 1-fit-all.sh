#! /bin/bash
# Olivier Julien, 2014
# ----------------------------

#\rm -r png; mkdir png;
\rm -r pdf; mkdir pdf;

for gracefile in ./data/*.dat; do
filename=$(basename "$gracefile")
extension="${filename##*.}"
filename="${filename%.*}"
 
#TMPPNG=${filename}_png.tmp
#cat $gracefile > $TMPPNG
#echo "#Print out to" >> $TMPPNG
#echo '@PRINT TO "'"${PWD}/png/${filename}.png"'"' >> $TMPPNG
#echo '@HARDCOPY DEVICE "PNG"' >> $TMPPNG
#echo '@PAGE SIZE 2000, 1500' >> $TMPPNG
#echo 'DEVICE "PNG" DPI 1200' >> $TMPPNG
#echo '@DEVICE "PNG" FONT ANTIALIASING on' >> $TMPPNG
#echo '# Make white background transparent' >> $TMPPNG
#echo '#@DEVICE "PNG" OP "transparent:on"' >> $TMPPNG
#echo '@DEVICE "PNG" OP "compression:9"' >> $TMPPNG
#echo '@PRINT' >> $TMPPNG
#/sw/lib/X11/grace/bin/xmgrace -geometry 1200x900 -nosafe $gracefile -hardcopy $TMPPNG -param param.par
 
#echo "$filename.$extension ->"
echo "$filename"

TMPPDF=${filename}_pdf.tmp
cat $gracefile > $TMPPDF
echo "#Print out to" >> $TMPPDF
echo '@PRINT TO "'"${PWD}/pdf/${filename}.pdf"'"' >> $TMPPDF
echo '@HARDCOPY DEVICE "PDF"' >> $TMPPDF
echo '@DEVICE "PDF" OP "PDF1.4"' >> $TMPPDF
echo '@PRINT' >> $TMPPDF
/opt/local/bin/xmgrace -geometry 1200x900 -nosafe $gracefile -hardcopy $TMPPDF -param param.par
done

\rm *.tmp;
