FROM ubuntu:22.04

WORKDIR /tmp
RUN apt-get update \
    && apt-get install -y -q ffmpeg git libfftw3-dev python3-pip \
    && apt-get clean \
    && apt-get autoremove -y

RUN git clone https://github.com/scivision/soothing-sounds.git
WORKDIR /tmp/soothing-sounds
RUN pip3 install -e .
RUN pip3 install ffmpeg-normalize~=1.27.7 librosa~=0.10.1 matplotlib~=3.7.0
WORKDIR /workspace
