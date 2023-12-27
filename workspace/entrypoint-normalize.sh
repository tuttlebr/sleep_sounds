#!/bin/bash
clear
WAVS=$(ls *.wav)
for WAV in ${WAVS};
do
    echo "Implement EBU R128 algorithm upon ${WAV}..."
    ffmpeg-normalize -f -pr ${WAV} --output "normalized-${WAV}"
    echo
done
