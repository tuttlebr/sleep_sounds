FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install -y -q cmake ffmpeg git libfftw3-dev libsndfile-dev \
    libtag1-dev python3-dev python3-pip python3-venv \
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
RUN apt install -y autoconf autogen automake build-essential libasound2-dev \
    libflac-dev libogg-dev libtool libvorbis-dev libopus-dev libmp3lame-dev \
    libmpg123-dev pkg-config
RUN git clone https://github.com/libsndfile/libsndfile.git
WORKDIR /tmp/libsndfile
RUN git checkout -b 1.2.2 \
    && mkdir CMakeBuild

WORKDIR /tmp/libsndfile/CMakeBuild
RUN cmake .. \
    && make \
    && make install \
    && cmake --build . \
    && python3 -m pip install pysndfile~=1.4.4 \
    && python3 -m pip install scikits.audiolab

RUN pip3 install ffmpeg-normalize~=1.27.7 librosa~=0.10.1 matplotlib~=3.7.0 pydub~=0.25.1 pyFFTW~=0.13.1
WORKDIR /workspace
