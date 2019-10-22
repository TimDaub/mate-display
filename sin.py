from machine import Pin, SPI
from display import Display
from utime import sleep_us
from math import sin
from urandom import randint
import _thread

def main(program):
    spi = SPI(
        1,
        baudrate=2000000,
        polarity=0,
        phase=0,
        firstbit=SPI.MSB,
        mosi=Pin(16),
        sck=Pin(17)
    )
    brightness = (int(program["brightness"])) / 100
    color = '%02x%02x%02x' % (
        randint(0, round(255 * brightness)),
        randint(0, round(255 * brightness)),
        randint(0, round(255 * brightness))
    )

    d = Display(spi, program["display"]["height"], program["display"]["width"])
    offset = 0
    while program["run"]:
        d.clear(False)
        for y in range(d.h):
            x = normalize(sin(y+offset), 0, 2) + 1
            d.set_pixel(x, y, color, False)

        offset += 1
        d.show()
        sleep_us(40000)

    d.clear()
    _thread.exit()

def normalize(x, minimum, maximum):
    sin_min = -1
    sin_max = 1
    return round((maximum - minimum) * ((x - sin_min)/(sin_max - sin_min)) + minimum)
