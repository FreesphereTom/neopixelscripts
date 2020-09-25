# Neopixel Morse code
import time
import board
import neopixel
import sys

num_pixels = int(30)
pixels = neopixel.NeoPixel(board.D18, 30)

# Times are built to international standards
dot_time = 0.3
dash_time = dot_time * 3
morse_time = dot_time
letter_time = dot_time * 2  # Standard is 3 units, but we are already waiting 1 unit in the code, so only doubling this
word_time = dot_time * 6  # Standard is 7 units, but we are already waiting 1 unit in the code, so only multiply by 6
load_word = sys.argv[1]
load_word = load_word.lower()
print(load_word)

def dot():
    pixels.fill((181, 2, 81))
    time.sleep(dot_time)
    pixels.fill((0, 0, 0))
    time.sleep(morse_time)


def dash():
    pixels.fill((181, 2, 81))
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
    dot()
    dot()
    dot()
    time.sleep(letter_time)


def i():
    dot()
    dot()
    time.sleep(letter_time)


def j():
    dot()
    dash()
    dash()
    dash()
    time.sleep(letter_time)


def k():
    dash()
    dot()
    dash()
    time.sleep(letter_time)


def l():
    dot()
    dash()
    dot()
    dot()
    time.sleep(letter_time)


def m():
    dash()
    dash()
    time.sleep(letter_time)


def n():
    dash()
    dot()
    time.sleep(letter_time)


def o():
    dash()
    dash()
    dash()
    time.sleep(letter_time)


def p():
    dot()
    dash()
    dash()
    dot()
    time.sleep(letter_time)


def q():
    dash()
    dash()
    dot()
    dash()
    time.sleep(letter_time)


def r():
    dot()
    dash()
    dot()
    time.sleep(letter_time)


def s():
    dot()
    dot()
    dot()
    time.sleep(letter_time)


def t():
    dash()
    time.sleep(letter_time)


def u():
    dot()
    dot()
    dash()
    time.sleep(letter_time)


def v():
    dot()
    dot()
    dot()
    dash()
    time.sleep(letter_time)


def w():
    dot()
    dash()
    dash()
    time.sleep(letter_time)


def x():
    dash()
    dot()
    dot()
    dash()
    time.sleep(letter_time)


def y():
    dash()
    dot()
    dash()
    dash()
    time.sleep(letter_time)


def z():
    dash()
    dash()
    dot()
    dot()
    time.sleep(letter_time)


options = {
    a: a,
    }


def morse(word):
    time.sleep(word_time)
    for xi in word:
        if xi == 'a':
            a()
        elif xi == 'b':
            b()
        elif xi == 'c':
            c()
        elif xi == 'd':
            d()
        elif xi == 'e':
            e()
        elif xi == 'f':
            f()
        elif xi == 'g':
            g()
        elif xi == 'h':
            h()
        elif xi == 'i':
            i()
        elif xi == 'j':
            j()
        elif xi == 'k':
            k()
        elif xi == 'l':
            l()
        elif xi == 'm':
            m()
        elif xi == 'n':
            n()
        elif xi == 'o':
            o()
        elif xi == 'p':
            p()
        elif xi == 'q':
            q()
        elif xi == 'r':
            r()
        elif xi == 's':
            s()
        elif xi == 't':
            t()
        elif xi == 'u':
            u()
        elif xi == 'v':
            v()
        elif xi == 'w':
            w()
        elif xi == 'x':
            x()
        elif xi == 'y':
            y()
        elif xi == 'z':
            z()
        else:
            pixels.fill((0, 0, 0))
            time.sleep(word_time)


while True:
    morse(list(load_word))
