#!/bin/bash
clear
rm -rf *.raw *.flac *.wav

for COLOR in white pink blue violet brown;
do
    echo "Generating ${COLOR} noise..."
    python3 soothing.py ${COLOR} -fs=44100 -nsec=600 -o ${COLOR}.raw
    ffmpeg -f s16le -ar 44100 -ac 1 -i ${COLOR}.raw ${COLOR}.wav
    echo
done
