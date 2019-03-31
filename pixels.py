from ubinascii import unhexlify

class Pixels:
    def __init__(self, spi, leds):
        self.spi = spi;
        self.leds = leds
        self.data = '000000' * self.leds

    def set_pixel(self, index, color):
        self.data = self.data[:index * 6] + color + self.data[index * 6 + 6:] 

    def set_display(self, display):
        self.data = display

    def set_range(self, index, offset, color):
        self.data = self.data[:index] + color + self.data[offset:]

    def show(self):
        self.spi.write(unhexlify(self.data))

    def clear(self):
        self.data = '000000' * self.leds
        self.spi.write(unhexlify(self.data))
