from machine import Pin, SPI
from display import Display
from utime import sleep_us

def iterative_lights():
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
    color = "f141f4"

    d = Display(spi, 8, 5)
    for col in range(0, d.w):
        for row in range(0, d.h):
            d.set_pixel(col, row, color)
            sleep_us(200000)

    d.clear()
    sleep_us(200000)

    for row in range(0, d.h):
        for col in range(0, d.w):
            d.set_pixel(col, row, color)
            sleep_us(200000)
