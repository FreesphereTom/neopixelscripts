# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

num_pixels = 30
pixels = neopixel.NeoPixel(board.D18, 30)


def strip(wait):
    for i in range(num_pixels):
        pixels[i] = (100, 0, 200)
        time.sleep(wait)
    for i in range(num_pixels):
        move = (29 - i)
        pixels[move] = (10, 120, 253)
        time.sleep(wait)


while True:
    strip(0.04)
