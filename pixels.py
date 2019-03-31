from machine import Pin, SPI
from unhexlify import ubinascii

class Pixels:
    def __init__(self, spi, leds):
        self.spi = spi;
        self.leds = leds
        self.empty = '000000' * self.leds
        self.data = self.empty

    def set_pixel(self, index, color):
        self.data = self.data[:index] + color + self.data[index + 6:] 

    def show(self):
        self.spi.write(unhexlify(self.data))

    def clear(self):
        self.spi.write(unhexlify(self.empty))
