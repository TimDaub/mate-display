from machine import Pin, SPI, ADC
from display import Display
from utime import sleep_us
from math import floor, pow

# doesn't work
def sound(pin):
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
    d.clear()
    adc = ADC(Pin(pin))

    color = '%02x%02x%02x' % (255, 255, 255)
    black = '0'*6
    for i in range(1000):
        v = adc.read()
        print("hello")
        print(v)
        l = floor(pow(2, floor(v/ 6)))
        if l > 100:
            if l > 1024:
                d.set_col(0, color, False)
            else:
                d.set_col(0, black, False)
            if l > 65536:
                d.set_col(1, color, False)
            else:
                d.set_col(1, black, False)
            if l > 33554432:
                d.set_col(2, color, False)
            else:
                d.set_col(2, black, False)
            if l > 8589934592:
                d.set_col(3, color, False)
            else:
                d.set_col(3, black, False)
            if l > 1125899906842624:
                d.set_col(4, color, False)
            else:
                d.set_col(4, black, False)

            d.show()
            sleep_us(100)
