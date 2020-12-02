import time
import board
import neopixel
import random
import colorsys
from threading import Thread


num_pixels = 30
pixels = neopixel.NeoPixel(board.D18, num_pixels)
pixel_range = list(range(0, num_pixels))
pixel_offset = num_pixels - 1
speed = 1
# multiplier to slow animations, can be float


def stripe_fill(wait, colour):
    for i in range(num_pixels):
        pixels[i] = colour
        time.sleep(wait)


def quick_fill(colour):
    pixels.fill(colour)


def speedup(tm, fillcolour, colours):
    for i in colours:
        stripe_fill(0.01 * tm, i)
        quick_fill(fillcolour)


def star_fill(tm, colour):
    global pixel_range
    random.shuffle(pixel_range)
    for i in pixel_range:
        pixels[i] = colour
        sleeptime = random.uniform(0, 0.5) * tm
        time.sleep(sleeptime)


def create_fades(colour, amount):
    colours = []
    r = colour[0]
    g = colour[1]
    b = colour[2]
    hsv_base = (colorsys.rgb_to_hsv(r, g, b))
    h = hsv_base[0]
    s = hsv_base[1]
    v = hsv_base[2]
    increase_by = 0
    for y in range(int(amount)):
        increase_by = increase_by + (v / amount)
        hsv_converted = colorsys.hsv_to_rgb(h, s, increase_by)
        r_new = hsv_converted[0]
        g_new = hsv_converted[1]
        b_new = hsv_converted[2]
        new_rgb = (round(r_new), round(g_new), round(b_new))
        colours.append(new_rgb)
    return colours


def flash(tm, colour, i):
    dm = random.uniform(1, 1.8)
    dim = tuple(c1 / dm for c1 in colour)
    sleeptime = random.uniform(0.5, 2) * tm
    colours = create_fades(dim, sleeptime * 25)
    for c in colours:
        pixels[i] = c
        time.sleep(sleeptime / len(colours) / 2)
    colours.reverse()
    for c in colours:
        pixels[i] = c
        time.sleep(sleeptime / len(colours) / 2)
    pixels[i] = (0, 0, 0)


def star_flash(tm, colours):
    global pixel_range
    t_end = time.time() + 5
    while time.time() < t_end:
        i = random.choice(pixel_range)
        colour = random.choice(colours)
        # Make sure pixel isn't already lit up
        if pixels[i] != [0, 0, 0]:
            continue
        global sft
        sft = Thread(target=flash, args=(tm, colour, i))
        sft.start()
        sleeptime = random.uniform(0.1, 0.4) * tm
        time.sleep(sleeptime)


def colour_chase_strip(colour, wait, last, pixel_length, stop):
    global cct_wait_next_animation
    global stop_threads_cct
    cct_wait_next_animation = True
    for i in range(num_pixels):
        if stop():
            break
        pixels[i] = colour
        time.sleep(wait)
        if last and i == pixel_length - 1:
            cct_wait_next_animation = False
            # pixels.fill((10, 10, 10))
            # cct.join()
            stop_threads_cct = True
            break


def colour_chase(tm, colours, pixel_length, repeat):
    last_n = repeat * len(colours)
    global stop_threads_cct
    stop_threads_cct = False
    n = 0
    for a in range(repeat):
        for i in colours:
            n += 1
            last = False
            if n == last_n:
                last = True
                stop = True
            pixel_speed = tm * 0.02
            global cct
            cct = Thread(target=colour_chase_strip, args=(i, pixel_speed, last, pixel_length, lambda: stop_threads_cct))
            cct.start()
            time.sleep(pixel_speed * pixel_length)


def central_wipe(tm, colour):
    for i in range(num_pixels // 2):
        pixels[(num_pixels // 2) + i] = colour
        pixels[(pixel_offset // 2) - i] = colour
        time.sleep(0.01 * tm)


def central_wipe_tailed():
    pass
    # some tail code


while True:
    # Fill then quickly stripe another colour
    # speedup(speed, (180, 180, 180), [(200, 10, 2), (4, 180, 2), (2, 4, 190)])
    # Fill to a solid colour, pixel by pixel
    # star_fill(speed, (200, 200, 200))
    # Random pixel flashes of varying brightnesses, like a starry sky
    # star_flash(speed, [(110, 100, 150), (220, 125, 125), (200, 200, 200), (220, 100, 100), (120, 125, 225)])
    # Chasing pixels, speed, colours, pixel length, repeat times
    # colour_chase(speed * 1.5, [(200, 10, 2), (4, 180, 2), (2, 4, 190)], 4, 5)
    # Starts from centre and lights up outwards, like lighting a sparkler from the middle
    # Works best with an even number of pixels
    # central_wipe(speed, (100, 100, 100))
    # Start by setting pixels to 0 as the star_flash animation only works on switched off pixels
    #

    # Bright loop
    # central_wipe(speed * 2, (0, 0, 0))
    # star_flash(speed, [(110, 100, 150), (220, 125, 125), (200, 200, 200), (220, 100, 100), (120, 125, 225)])
    # while sft.is_alive():
    #     # wait for animations to finish by waiting for threads to end
    #     pass
    #
    # colour_chase(speed * 2, [(169, 12, 12), (200, 200, 200), (20, 169, 20), (200, 200, 200)], 6, 5)
    # while cct_wait_next_animation:
    #     # wait for animation to confirm completion. This is glitchy and on faster runs can cause clashing
    #     # but since I know next to no Python, this is the best we're getting today
    #     pass
    # # Play catch up because the timing gets out of whack due to my poor Python skills (edit: possibly fixed by moving
    # # break higher)
    # time.sleep(0.005)
    #
    # for x in range(4):
    #     central_wipe(speed * 1.5, (140, 180, 200))
    #     central_wipe(speed * 1.5, (100, 100, 100))
    #     central_wipe(speed * 1.5, (0, 0, 0))
    #
    #     central_wipe(speed * 1.5, (251, 202, 39))
    #     central_wipe(speed * 1.5, (100, 100, 100))
    #     central_wipe(speed * 1.5, (0, 0, 0))
    #
    #     central_wipe(speed * 1.5, (120, 30, 180))
    #     central_wipe(speed * 1.5, (100, 100, 100))
    #     central_wipe(speed * 1.5, (0, 0, 0))

    # Dim loop
    central_wipe(speed * 2, (0, 0, 0))
    star_flash(speed, [(50, 40, 40), (40, 40, 50), (30, 30, 30)])
    while sft.is_alive():
        # wait for animations to finish by waiting for threads to end
        pass

    colour_chase(speed * 2, [(50, 2, 2), (20, 20, 20), (2, 69, 2), (20, 20, 20)], 6, 5)
    while cct_wait_next_animation:
        # wait for animation to confirm completion. This is glitchy and on faster runs can cause clashing
        # but since I know next to no Python, this is the best we're getting today
        pass
    # Play catch up because the timing gets out of whack due to my poor Python skills (edit: possibly fixed by moving
    # break higher)
    time.sleep(0.005)

    for x in range(4):
        central_wipe(speed * 1.5, (14, 18, 40))
        central_wipe(speed * 1.5, (20, 20, 20))
        central_wipe(speed * 1.5, (0, 0, 0))

        central_wipe(speed * 1.5, (30, 4, 1))
        central_wipe(speed * 1.5, (20, 20, 20))
        central_wipe(speed * 1.5, (0, 0, 0))

        central_wipe(speed * 1.5, (22, 5, 22))
        central_wipe(speed * 1.5, (20, 20, 20))
        central_wipe(speed * 1.5, (0, 0, 0))