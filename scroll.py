import json
from machine import Pin, SPI
from display import Display
from utime import sleep_us
from text import Text
import _thread

def main(program):
    spi = SPI(
        1,
        baudrate=2000000,
        polarity=0,
        phase=0,
        firstbit=SPI.MSB,
        mosi=Pin(16),
        sck=Pin(17)
    )

    d = Display(spi, 8, 5)
    #t = Text(d, program["text"])
    t =  Text(d, program["text"])
    t.scroll(1, int(program["speed"]))
    _thread.exit()
