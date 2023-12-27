from argparse import ArgumentParser

import librosa
import librosa.display
import matplotlib.pyplot as plt


def main():
    P = ArgumentParser(
        description=
        "noise visualizer program for Raspberry Pi or any Python-capable computer"
    )
    P.add_argument(
        "wavpath",
        help="file location for noise wav file.",
        nargs="?",
        default="pink.wav",
    )
    P.add_argument(
        "-nsec",
        help="length of unique noise sequence [seconds]",
        type=float,
        default=60,
    )
    p = P.parse_args()

    fig, ax = plt.subplot_mosaic("hSSS;hSSS;hSSS;.vvv")
    y, sr = librosa.load(p.wavpath, duration=p.nsec)
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    sim = librosa.segment.recurrence_matrix(chroma, mode='affinity')
    librosa.display.specshow(sim,
                             ax=ax['S'],
                             sr=sr,
                             x_axis='time',
                             y_axis='time',
                             auto_aspect=False)
    ax['S'].label_outer()
    ax['S'].sharex(ax['v'])
    ax['S'].sharey(ax['h'])
    ax['S'].set(title='Self-similarity')
    librosa.display.waveshow(y, ax=ax['v'])
    ax['v'].label_outer()
    ax['v'].set(title='transpose=False')
    librosa.display.waveshow(y, ax=ax['h'], transpose=True)
    ax['h'].label_outer()
    ax['h'].set(title='transpose=True')

    plt.savefig(f"{p.wavpath}.png", dpi=300)


if __name__ == "__main__":
    main()
