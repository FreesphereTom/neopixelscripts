# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

num_pixels = int(30)
pixels = neopixel.NeoPixel(board.D18, 30)


def strip(wait):
    for i in range(num_pixels // 2):
        pixels[(num_pixels // 2) + i] = (100, 0, 200)
        pixels[(num_pixels // 2) - i] = (100, 0, 200)
        time.sleep(wait)
    for i in range(num_pixels // 2):
        pixels[(num_pixels // 2) + i] = (255, 0, 200)
        pixels[(num_pixels // 2) - i] = (255, 0, 200)
        time.sleep(wait)


while True:
    strip(0.04)
