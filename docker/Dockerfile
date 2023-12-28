FROM ubuntu:22.04

RUN apt-get update \
    && apt install -y -q autoconf autogen automake build-essential cmake ffmpeg \
    git libasound2-dev libfftw3-dev libtag1-dev python3-dev  libflac-dev \
    libogg-dev libtool libvorbis-dev libopus-dev libmp3lame-dev \
    libmpg123-dev libsndfile1-dev libsndfile1 pkg-config python3-pip python3-venv \
    && apt-get clean \
    && apt-get autoremove -y

WORKDIR /tmp
RUN git clone https://github.com/scivision/soothing-sounds.git
WORKDIR /tmp/soothing-sounds
RUN git checkout -b v1.0.2 \
    && pip3 install -e .

WORKDIR /tmp
RUN git clone https://github.com/supermihi/pytaglib.git
WORKDIR /tmp/pytaglib
RUN git checkout -b v2.1.0 \
    && pip3 install -e .

WORKDIR /tmp
RUN pip3 install ffmpeg-normalize~=1.27.7 librosa~=0.10.1 matplotlib~=3.7.0 pydub~=0.25.1 pyFFTW~=0.13.1
WORKDIR /workspace
