#!/bin/bash
FILE=laplace_data/meta.txt
for i in {0..66}
do
  VAL="2^(-$i)"
  VAL=$(bc -l <<< $VAL)
  echo "Running iteration $i..."
  echo "------------------------------------" >> $FILE
  echo "alpha=$VAL" >> $FILE
  echo "NON-STEMMED" >> $FILE
  python3.7 mp4.py --laplace $VAL >> $FILE
  echo "STEMMED" >> $FILE
  python3.7 mp4.py --stemming --laplace $VAL >> $FILE
done
