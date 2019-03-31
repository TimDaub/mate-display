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
        if y % 2 == 0:
            index = x + self.w * y
        else:
            index = self.w * y + self.w - x - 1
        self.p.set_pixel(index, color) 
        self.p.show()

    def set_row(self, row, color, show=True):
        # NOTE: We could do this with self.set_pixel
        colors = color * self.w
        offset = 6 * self.w
        self.p.set_range(row * offset, row * offset + len(colors), colors)
        if show:
            self.p.show()

    def set_col(self, col, color, show=True):
        for i in range(0, self.h):
            self.set_pixel(col, i, color)
        if show:
            self.p.show()

    def show(self):
        self.p.show()

    def clear(self):
        self.p.clear()

