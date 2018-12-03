#!/bin/sh

# append to file to make it a bit bigger
a=0
while [ $a -lt 100 ]
do
   echo $a
   # cat 1513-0.txt >> python/temp.txt
   cat test.txt >> python/temp.txt
   a=`expr $a + 1`
done

cd python 
python countPool.py temp.txt temp.txt temp.txt temp.txt temp.txt temp.txt temp.txt temp.txt temp.txt temp.txt 

# remove the tmp file
rm temp.txt