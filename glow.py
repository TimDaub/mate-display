from utime import sleep_us

class Glow:
    def __init__(self, d, timeout=200):
        self.d = d
        self.timeout = timeout

    def set_pixel(self, x, y, r, g, b):
        for i in range(r or g or b):
            if r:
                color = '%02x%02x%02x' % (i, g, b)
            if g:
                color = '%02x%02x%02x' % (r, i, b)
            if b:
                color = '%02x%02x%02x' % (r, g, i)

            self.d.set_pixel(x, y, color)
            sleep_us(self.timeout)

    def clear_pixel(self, x, y):
        color = self.d.get_color(x, y)
        (r, g, b) = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        for i in reversed(range(r or g or b)):
            if r:
                color = '%02x%02x%02x' % (i, g, b)
            if g:
                color = '%02x%02x%02x' % (r, i, b)
            if b:
                color = '%02x%02x%02x' % (r, g, i)

            self.d.set_pixel(x, y, color)
            sleep_us(self.timeout)


            



