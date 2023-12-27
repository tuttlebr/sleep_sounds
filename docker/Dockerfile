FROM ubuntu:22.04

WORKDIR /tmp
RUN apt-get update \
    && apt-get install -y -q ffmpeg git libfftw3-dev python3-pip \
    && apt-get clean \
    && apt-get autoremove -y

RUN git clone https://github.com/scivision/soothing-sounds.git
WORKDIR /tmp/soothing-sounds
RUN pip3 install -e .

WORKDIR /workspace
