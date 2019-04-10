from machine import Pin, SPI
from display import Display
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

    d = Display(spi, program["display"]["height"], program["display"]["width"])
    t =  Text(d, program["text"])
    t.scroll(1, int(program["speed"]))
    _thread.exit()
