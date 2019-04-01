from utime import sleep_us
from urandom import randint

class Glow:
    def __init__(self, d, timeout=200):
        self.d = d
        self.timeout = timeout
        self.pixels = []


    def set_pixel(self, x, y):
        self.pixels.append([x, y, randint(0, 254), randint(0, 254), randint(0, 254)])

    def tick(self):
        for pixel in self.pixels:
            self.d.set_pixel(pixel[0], pixel[1], '%02x%02x%02x' % (pixel[2], pixel[3], pixel[4]), False)
            if pixel[2] > 0:
                pixel[2] -= 1
            if pixel[3] > 0:
                pixel[3] -= 1
            if pixel[4] > 0:
                pixel[4] -= 1
        self.d.show()


            



