from machine import Pin, SPI
from display import Display
from pixels import Pixels
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

    d = Display(spi, 4, 5)
    for col in range(0, 5):
        for row in range(0, 4):
            d.set_pixel(col, row, color)
            sleep_us(200000)

    d.clear()
    sleep_us(200000)

    for row in range(0, 4):
        for col in range(0, 5):
            d.set_pixel(col, row, color)
            sleep_us(200000)
