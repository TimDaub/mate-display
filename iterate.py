from machine import Pin, SPI
from display import Display
from pixels import Pixels
from utime import sleep_us

def iterative_lights():
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
    p = Pixels(spi, 20)
    p.set_pixel(0, color)
    while(True):
        for i in range(0, 20):
            p.set_pixel(i, color)
            p.show()
            sleep_us(200000)
        p.clear()
        sleep_us(200000)

    ##d = Display(spi, 4, 5)
    ##for row in range(0, 4):
    ##    for col in range(0, 3):
    ##        d.set_pixel(row, col, color)
    ##        sleep_us(2000)
            

