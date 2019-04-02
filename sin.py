from machine import Pin, SPI
from display import Display
from utime import sleep_us
from math import sin
from urandom import randint

pill = False

def set_pill(p):
    pill = p

# sin_wave(100, 100000) is nice
def sin_wave(iterations, rate):
    spi = SPI(
        1,
        baudrate=2000000,
        polarity=0,
        phase=0,
        firstbit=SPI.MSB,
        mosi=Pin(16),
        sck=Pin(17)
    )
    sleep_us(200000)
    color = '%02x%02x%02x' % (randint(0, 254), randint(0, 254), randint(0, 254))

    d = Display(spi, 8, 5)
    for offset in range(iterations):
        if pill:
            break

        d.clear()
        for y in range(d.h):
            x = normalize(sin(y+offset), 0, 2) + 1
            d.set_pixel(x, y, color, False)

        d.show()
        sleep_us(rate)


def normalize(x, minimum, maximum):
    sin_min = -1
    sin_max = 1
    return round((maximum - minimum) * ((x - sin_min)/(sin_max - sin_min)) + minimum)
