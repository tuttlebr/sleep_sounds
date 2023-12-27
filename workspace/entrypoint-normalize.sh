#!/bin/bash
clear
rm -f normalized*.wav *.png
WAVS=$(ls *.wav)

ffmpeg-normalize -f -pr --dual-mono \
    blue.wav brown.wav pink.wav violet.wav white.wav \
    --output normalized-blue.wav normalized-brown.wav normalized-pink.wav normalized-violet.wav normalized-white.wav
