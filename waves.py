from machine import Pin, SPI
from display import Display
from utime import sleep_us

def waves():
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
    for i in range(0, 20):
        d.set_row(i % d.w, color)
        sleep_us(200000)
        d.clear()

    sleep_us(200000)

    for j in range(0, 20):
        d.set_col(j % d.h, color)
        sleep_us(200000)
        d.clear()
