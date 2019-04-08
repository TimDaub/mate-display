from machine import Pin, SPI
from display import Display
from glow import Glow
from utime import sleep_us
from urandom import randint

def random(iterations, factor):
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

    d = Display(spi, 12, 5)
    g = Glow(d)

    pixels = []
    for i in range(iterations):
        if randint(0, 100) % factor == 0:
            g.set_pixel(randint(0, d.w-1), randint(0, d.h-1))
        g.tick()
        sleep_us(1)
