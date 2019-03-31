from machine import Pin, SPI
from pixels import Pixels
from utime import sleep_us
from random import randint

def glow():
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

    p = Pixels(spi, 20)
    # warning, this doesn't allow the esp32 to be pushed to anymore
    for i in range(0, 50):
        h = randint(0, 16777215)
        color = hex(h)[2:]
        color += '0' * (6 - len(color))
        display = color * 20
        p.set_display(display)
        p.show()
        sleep_us(100000)
