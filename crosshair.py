from machine import Pin, SPI
from display import Display
from utime import sleep_us
from urandom import getrandbits

def crosshair():
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
    x = 0
    y = 0
    for i in range(0, 20):
        #d.set_row(x, color)
        #d.set_col(y, color)
        d.set_pixel(x, y, color)
        d.show()
        sleep_us(500000)
        d.clear()

        dx = bool(getrandbits(1))
        dy = bool(getrandbits(1))

        if dx:
            x += 1
        else:
            x -= 1

        if dy:
            y += 1
        else:
            y -= 1

        if x > 4:
            x -= 1
        elif x < 0:
            x += 1
        
        if y > 3:
            y -= 1
        else:
            y += 1
