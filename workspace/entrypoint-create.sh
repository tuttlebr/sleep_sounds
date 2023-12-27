#!/bin/bash
clear
rm -rf *.png *.raw *.flac *.wav
SAMPLERATE=16000
NHOUR=8
NSEC=60

for COLOR in blue brown pink violet white;
do
    echo "Generating ${COLOR} noise..."
    python3 soothing.py ${COLOR} ${NHOUR} -fs=${SAMPLERATE} -nsec=${NSEC} -o=${COLOR}.flac
    echo
done
python3 visualize.py
python3 tag.py
