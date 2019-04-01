import json
from machine import Pin, SPI
from display import Display
from utime import sleep_us
from text import Text

def scroll(text):
    spi = SPI(
        1,
        baudrate=2000000,
        polarity=0,
        phase=0,
        firstbit=SPI.MSB,
        mosi=Pin(16),
        sck=Pin(17)
    )

    d = Display(spi, 4, 5)
    t = Text(d, text)
    t.set_letter(0)
    d.show()
    sleep_us(1000000)
    t.offset(1, 0)
    d.show()
    sleep_us(1000000)
    t.offset(1, 0)
    d.show()

