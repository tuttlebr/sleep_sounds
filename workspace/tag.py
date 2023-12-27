import os
from datetime import datetime
from glob import glob

import taglib

wav_files = glob("*.wav")

for wav_file in wav_files:
    title = os.path.splitext(wav_file)[0]
    METADATA = {
        "ARTIST": ["Brandon Tuttle"],
        "ALBUM": ["Sleep Sounds"],
        "TITLE": [title],
        "GENRE": ["Ambient"],
        "DATE": [str(datetime.now().year)],
    }
    with taglib.File(wav_file, save_on_exit=True) as song:
        song.tags = METADATA
        print(song.tags)
