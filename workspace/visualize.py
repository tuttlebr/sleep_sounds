import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from colour import RGB, rgb2hex


def colorFader(
        c1,
        c2,
        mix=0
):  #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1 = np.array(mpl.colors.to_rgb(c1))
    c2 = np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1 - mix) * c1 + mix * c2)


colors = {
    "blue": [RGB.BLUE, RGB.NAVY],
    "brown": [RGB.SANDYBROWN, RGB.SADDLEBROWN],
    "pink": [RGB.PINK, RGB.DEEPPINK],
    "violet": [RGB.VIOLET, RGB.BLUEVIOLET],
    "white": [RGB.WHITE, RGB.LIGHTSLATEGRAY]
}

for color in colors:
    n = 500
    c1 = rgb2hex(colors[color][0])
    c2 = rgb2hex(colors[color][1])
    fig, ax = plt.subplots(figsize=(8, 8), frameon=False, dpi=300)
    ax.set_axis_off()
    for x in range(n + 1):
        ax.axvline(x, color=colorFader(c1, c2, x / n))
    plt.savefig(f"{color}-artwork.png")
