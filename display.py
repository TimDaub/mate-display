from pixels import Pixels

class Display:
    def __init__(self, spi, h, w):
        self.p = Pixels(spi, h*w)
        self.h = h
        self.w = w

    def set_pixel(self, x, y, color):
        # Our display is wired where odd rows go from left to right
        # and even rows go from right to left
        index = 0
        if x % 2 == 0:
            index = x + (self.w * y)
        else:
            index = x - self.w + self.w * y
        self.p.set_pixel(index, color) 
        self.p.show()

