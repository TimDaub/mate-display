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

    d = Display(spi, 4, 5)
    for i in range(0, 20):
        row = i % 4
        col = i % 5
        d.set_row(row, color)
        d.set_row(3-row, color)
        d.set_col(col, color)
        d.set_col(4-col, color)
        sleep_us(200000)
        d.clear()
