#!/bin/bash
FILE=laplace_data/meta.txt
for i in {1..50}
do
  echo "Running iteration $i..."
  echo "------------------------------------" >> $FILE
  echo "alpha=$i" >> $FILE
  echo "NON-STEMMED" >> $FILE
  python3.7 mp4.py --laplace $i >> $FILE
  echo "STEMMED" >> $FILE
  python3.7 mp4.py --stemming --laplace $i >> $FILE
done
