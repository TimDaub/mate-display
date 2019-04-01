from machine import Pin, SPI
from display import Display
from glow import Glow
from utime import sleep_us
from urandom import randint

def random():
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
    color = "f"*6

    d = Display(spi, 8, 5)
    g = Glow(d)
    g.set_pixel(0, 0, 0, 255, 0)
