import json
from machine import Pin, SPI
from display import Display
from utime import sleep_us

def char_replace(string):
    dotstring = ''
    with open('dotfont.json') as fh:
        dotfont = json.load(fh)
        for char in string:
            dotchar = dotfont[char.upper()]
            dotstring = dotstring + dotchar[1:] + "....."
    return(dotstring)

def dotmatrixtext(text):
    spi = SPI(
        1,
        baudrate=2000000,
        polarity=0,
        phase=0,
        firstbit=SPI.MSB,
        mosi=Pin(16),
        sck=Pin(17)
    )
    color = "f141f4"

    d = Display (spi, 4, 5)
    dotstring = char_replace(text)
    i = 0
    col = 0
    row = 0
    for char in dotstring:
        col += 1
        d.set_pixel(col, row, color)
        if col == 4
            row += 1
            col = 0

dotmatrixtext("A")