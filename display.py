from pixels import Pixels

class Display:
    def __init__(self, spi, h, w):
        self.p = Pixels(spi, h*w)
        self.h = h
        self.w = w

    def get_pixel(self, x, y):
        index = 0
        if y % 2 == 0:
            # wiring: top left to bottom
            #index = x + self.w * y
            #rewiring from bottom left to top left:
            index = (self.w * self.h - 1) - (x + self.w * y)
        else:
            # wiring: top left to bottom
            #index = self.w * y + self.w - x - 1
            #rewiring from bottom left to top left
            index = (self.w * self.h) - (self.w * y + (self.w - x))
        return index

    def get_color(self, x, y):
        return self.p.get_pixel(self.get_pixel(x, y))

    def set_pixel(self, x, y, color, show=True):
        if x > self.w or x < 0 or y > self.h or y < 0:
            # TODO: Make IndexValue error
            raise Exception("Out of index")
        else:
            index = self.get_pixel(x, y)
            self.p.set_pixel(index, color) 
            if show:
                self.p.show()

    # NOTE: Probably outdated with rewiring
    def set_row(self, row, color, show=True):
        # NOTE: We could do this with self.set_pixel
        colors = color * self.w
        offset = 6 * self.w
        self.p.set_range(row * offset, row * offset + len(colors), colors)
        if show:
            self.p.show()

    # NOTE: Probably outdated with rewiring
    def set_col(self, col, color, show=True):
        for i in range(0, self.h):
            self.set_pixel(col, i, color)
        if show:
            self.p.show()

    def set_data(self, data):
        self.p.set_data(data)

    def show(self):
        self.p.show()

    def clear(self):
        self.p.clear()

