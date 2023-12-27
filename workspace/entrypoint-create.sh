#!/bin/bash
clear
rm -rf *.png *.raw *.flac *.wav normalized
SAMPLERATE=16000
NHOUR=1
NSEC=1800

for COLOR in blue brown pink violet white;
do
    echo "Generating ${COLOR} noise..."
    python3 soothing.py ${COLOR} ${NHOUR} -fs=${SAMPLERATE} -nsec=${NSEC} -o=${COLOR}.raw
    ffmpeg -f s16le -ar ${SAMPLERATE} -ac 1 -i ${COLOR}.raw ${COLOR}.wav
    python3 visualize.py ${COLOR}.wav -nsec=${NSEC}
    echo
done
