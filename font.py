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
            dotstring += dotchar
    return dotstring

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

    d = Display (spi, 4, 5)
    dotstring = char_replace(text)
    denominator = 25
    chunks = [dotstring[i:i+denominator] for i in range(0, len(dotstring), denominator)]
    for chunk in chunks:
        col = 0
        row = 0
        for char in chunk:
            if col == 5:
                row += 1
                col = 0
            if char == "X":
                d.set_pixel(col, row, 'f'*6)
            else:
                d.set_pixel(col, row, '0'*6)
            col += 1
        d.show()
        sleep_us(2000000)
        d.clear()
