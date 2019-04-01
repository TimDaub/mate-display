from machine import Pin, SPI
from display import Display
from pixels import Pixels

def rgb2hex(r, g, b):
    "{0:02x}{1:02x}{2:02x}".format(r, g, b)

def colorwheel():
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
    r = 255
    g = 0
    b = 0
    color = rgb2hex(r, g, b)

    while b < 256:
        # adding blue
        display = color * 40
        d.set_display(display)
        p.show()
        b += 1

    while r > 0:
        # subtracting red
        display = color * 40
        p.set_display(display)
        p.show()
        r += -1

    while g < 256:
        # adding green
        display = color * 40
        p.set_display(display)
        p.show()
        g += 1

    while b > 0:
        # subtracting blue
        display = color * 40
        p.set_display(display)
        p.show()
        b += -1

    while b < 256:
        # adding red
        display = color * 40
        p.set_display(display)
        p.show()
        r += 1

    while g > 0:
        # subtracting green
        display = color * 40
        p.set_display(display)
        p.show()
        g += -1
