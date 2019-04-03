from machine import Pin, SPI
from display import Display
from utime import sleep_us
from math import sin, floor
from urandom import randint
import _thread
import utime

def main(program):
    fps = int(program["fps"])
    spi = SPI(
        1,
        baudrate=2000000,
        polarity=0,
        phase=0,
        firstbit=SPI.MSB,
        mosi=Pin(16),
        sck=Pin(17)
    )
    color = '%02x%02x%02x' % (randint(0, 254), randint(0, 254), randint(0, 254))

    d = Display(spi, 8, 5)
    offset = 0
    frames = 0
    begin = utime.ticks_ms()
    while program["run"]:
        d.clear(False)
        for y in range(d.h):
            x = normalize(sin(y+offset), 0, 2) + 1
            d.set_pixel(x, y, color, False)

        offset += 1
        d.show()

        if utime.ticks_ms() - begin > 1000*600:
            frames = 0
            begin = utime.ticks_ms()
        else:
            frames += 1
        s = floor(frames/fps)

        sleep_us(s)
    _thread.exit()

def normalize(x, minimum, maximum):
    sin_min = -1
    sin_max = 1
    return round((maximum - minimum) * ((x - sin_min)/(sin_max - sin_min)) + minimum)
