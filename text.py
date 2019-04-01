import json
from display import Display
from utime import sleep_us

class Text:
    def __init__(self, display, text):
        self.display = display
        self.text = text

    def encode(self):
        dotstring = ''
        with open('dotfont.json') as fh:
            dotfont = json.load(fh)
            for char in self.text:
                dotchar = dotfont[char.upper()]
                dotstring += dotchar
        return dotstring

    def set_letter(self, index, x=0, y=0):
        dotstring = self.encode()
        # TODO: Change this name
        splitter = 25
        letters = [dotstring[i:i+splitter]
                    for i in range(0, len(dotstring), splitter)]
        letter = letters[index]
        row = x
        col = y
        for pixel in letter:
            if col == self.display.w:
                row += 1
                col = 0
            if pixel == "X":
                try:
                    self.display.set_pixel(col, row, 'f'*6, False)
                except Exception:
                    pass
            else:
                try:
                    self.display.set_pixel(col, row, '0'*6, False)
                except Exception:
                    pass
            col += 1

    def scroll(self, space=1, speed=100000):
        length = len(self.text)
        length += length * 5 * space
        for x in range(0, length):
            sleep_us(speed)
            for index in range(0, len(self.text)):
                self.set_letter(index, x-(index*5+index*space), 0)
            self.display.show()
            self.offset(0, 1)

    def offset(self, dx, dy):
        # NOTE: This is a really bad implementation. I currently don't know how
        # to improve it, however.
        d = Display(self.display.p.spi, self.display.h, self.display.w)
        for y in range(0, self.display.h):
            for x in range(0, self.display.w):
                color = self.display.get_color(x, y)
                # NOTE: We set the pixels on the Display copy here as we're
                # otherwise overwriting the old display's pixels.
                try:
                    d.set_pixel(x+dx, y+dy, color, False)
                except Exception:
                    pass
                self.display.set_pixel(x, y, '0' * 6, False)
        # Now we replace the old display with the new one
        self.display.set_data(d.p.data)
