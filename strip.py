import time
import board
import neopixel
import sys

num_pixels = 30
pixels = neopixel.NeoPixel(board.D18, 30)


def strip(wait, colour):
    r = 1
    for c in colour:
        if (r % 2) == 0:
            for i in range(num_pixels):
                pixels[i] = c
                time.sleep(wait)
        else:
            for i in range(num_pixels):
                move = (num_pixels - 1 - i)
                pixels[move] = c
                time.sleep(wait)
        r += 1


if len(sys.argv) > 1:
    h_in = sys.argv[1]
else:
    h_in = input('Enter comma separated hex list: ')


h_in = h_in.replace("#", "")
h_in = h_in.replace(" ", "")
h_ins = h_in.split(",")
colours = []
for h in h_ins:
    RGB = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    colours.append(RGB)


while True:
    strip(0.04, colours)