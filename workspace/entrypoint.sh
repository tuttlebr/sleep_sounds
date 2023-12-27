#!/bin/bash
clear
rm -rf *.raw *.flac *.wav
SAMPLERATE=16000
NSEC=600

for COLOR in white pink blue violet brown;
do
    echo "Generating ${COLOR} noise..."
    python3 soothing.py ${COLOR} -fs=${SAMPLERATE} -nsec=${NSEC} -o ${COLOR}.raw
    ffmpeg -f s16le -ar ${SAMPLERATE} -ac 1 -i ${COLOR}.raw ${COLOR}.wav
    echo
done
