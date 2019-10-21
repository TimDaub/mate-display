from machine import Pin, SPI
from utime import sleep_us

from display import Display

# A program to clean the screen in a stylish manner
def main():
    sleep_us(500000)
    spi = SPI(
        1,
        baudrate=2000000,
        polarity=0,
        phase=0,
        firstbit=SPI.MSB,
        mosi=Pin(16),
        sck=Pin(17)
    )
    black = "0"*6*100
    white = "f"*6*100

    d = Display(spi, 20, 5)
    d.set_data(white)
    d.show()
    sleep_us(50000)
    d.set_data(black)
    d.show()
    sleep_us(50000)
    d.set_data(white)
    d.show()
    sleep_us(50000)
    d.set_data(black)
    d.show()
    sleep_us(50000)

