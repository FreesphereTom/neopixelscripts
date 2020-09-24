# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

num_pixels = int(30)
pixels = neopixel.NeoPixel(board.D18, 30)

dot_time = 0.3
dash_time = 0.9
morse_time = 0.3
letter_time = 0.9
word_time = 1.8
word = 'AbC DeF'
word = word.lower()


def dot():
    pixels.fill((255, 255, 255))
    time.sleep(dot_time)
    pixels.fill((0, 0, 0))
    time.sleep(morse_time)


def dash():
    pixels.fill((255, 255, 255))
    time.sleep(dash_time)
    pixels.fill((0, 0, 0))
    time.sleep(morse_time)


def a():
    dot()
    dash()
    time.sleep(letter_time)


def b():
    dash()
    dot()
    dot()
    dot()
    time.sleep(letter_time)


def c():
    dash()
    dot()
    dash()
    dot()
    time.sleep(letter_time)


def d():
    dash()
    dot()
    dot()
    time.sleep(letter_time)


def e():
    dot()
    time.sleep(letter_time)


def f():
    dot()
    dot()
    dash()
    dot()
    time.sleep(letter_time)


def g():
    dash()
    dash()
    dot()
    time.sleep(letter_time)


def h():
    dot()
    time.sleep(letter_time)


def i():
    dot()
    time.sleep(letter_time)


def j():
    dot()
    time.sleep(letter_time)


def k():
    dot()
    time.sleep(letter_time)


def l():
    dot()
    time.sleep(letter_time)


def m():
    dot()
    time.sleep(letter_time)


def n():
    dot()
    time.sleep(letter_time)


def o():
    dot()
    time.sleep(letter_time)


def p():
    dot()
    time.sleep(letter_time)


def q():
    dot()
    time.sleep(letter_time)


def r():
    dot()
    time.sleep(letter_time)


def s():
    dot()
    time.sleep(letter_time)


def t():
    dot()
    time.sleep(letter_time)


def u():
    dot()
    time.sleep(letter_time)


def v():
    dot()
    time.sleep(letter_time)


def w():
    dot()
    time.sleep(letter_time)


def x():
    dot()
    time.sleep(letter_time)


def y():
    dot()
    time.sleep(letter_time)


def z():
    dot()
    time.sleep(letter_time)


options = {
    a: a,
    }


def morse(word):
    for x in word:
        if x == 'a':
            a()
        elif x == 'b':
            b()
        elif x == 'c':
            c()
        elif x == 'd':
            d()
        elif x == 'e':
            e()
        elif x == 'f':
            f()
        elif x == 'g':
            g()
        elif x == 'h':
            h()
        elif x == 'i':
            i()
        elif x == 'j':
            j()
        elif x == 'k':
            k()
        elif x == 'l':
            l()
        elif x == 'm':
            m()
        elif x == 'n':
            n()
        elif x == 'o':
            o()
        elif x == 'p':
            p()
        elif x == 'q':
            q()
        elif x == 'r':
            r()
        elif x == 's':
            s()
        elif x == 't':
            t()
        elif x == 'u':
            u()
        elif x == 'v':
            v()
        elif x == 'w':
            w()
        elif x == 'x':
            x()
        elif x == 'y':
            y()
        elif x == 'z':
            z()
        else:
            time.sleep(word_time)


while True:
    morse(list(word))
