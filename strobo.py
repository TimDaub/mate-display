from machine import Pin, SPI
from display import Display
from utime import sleep_us
from urandom import randint

# strobo(1000, 60000) is a good value
def strobo(iterations, sleep):
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
    black = '0'*6*d.w*d.h
    on = True
    for i in range(iterations):
        color = '%02x%02x%02x' % (randint(0, 254), randint(0, 254), randint(0, 254))
        if on:
            d.set_data(color*d.w*d.h)
        else:
            d.set_data(black)
        on = not on
        d.show()
        sleep_us(sleep)
