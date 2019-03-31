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
    sleep_us(200000)
    color = "f141f4"
    ##p = Pixels(spi, 20)
    ##while(True):
    ##    for i in range(0, 20):
    ##        p.set_pixel(i, color)
    ##        p.show()
    ##        sleep_us(200000)
    ##    p.clear()
    ##    sleep_us(200000)

    d = Display(spi, 4, 5)
    for col in range(0, 5):
        for row in range(0, 4):
            d.set_pixel(col, row, color)
            sleep_us(200000)
    d.clear()
    sleep_us(200000)

    for row in range(0, 4):
        for col in range(0, 5):
            d.set_pixel(col, row, color)
            sleep_us(200000)
    #d.set_pixel(0, 0, color)
    #sleep_us(200000)
    #d.set_pixel(1, 0, color)
    #sleep_us(200000)
    #d.set_pixel(2, 0, color)
    #sleep_us(200000)
    #d.set_pixel(3, 0, color)
    #sleep_us(200000)
    #d.set_pixel(4, 0, color)
    #sleep_us(200000)

    #d.set_pixel(0, 2, color)
    #sleep_us(200000)
    #d.set_pixel(1, 2, color)
    #sleep_us(200000)
    #d.set_pixel(2, 2, color)
    #sleep_us(200000)
    #d.set_pixel(3, 2, color)
    #sleep_us(200000)
    #d.set_pixel(4, 2, color)
    #sleep_us(200000)

    #d.set_pixel(0, 1, color)
    #sleep_us(200000)
    #d.set_pixel(1, 1, color)
    #sleep_us(200000)
    #d.set_pixel(2, 1, color)
    #sleep_us(200000)
    #d.set_pixel(3, 1, color)
    #sleep_us(200000)
    #d.set_pixel(4, 1, color)
    #sleep_us(200000)


