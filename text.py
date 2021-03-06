import json
from utime import sleep_us


class Text:
    def __init__(self, display, text):
        self.display = display
        self.text = text.strip()
        self.dotstring = self.encode()

    def encode(self):
        dotstring = ''
        with open('dotfont.json') as fh:
            dotfont = json.load(fh)
            for char in self.text:
                if char.isspace():
                    dotstring += ("." * 10)
                else:
                    dotchar = dotfont[char.upper()] + ("." * 5)
                    dotstring += dotchar
        return dotstring

    def add_spaces(self, spaces):
        s = '.'*self.display.w*spaces
        dotstring = ""
        for i in range(0, len(self.dotstring), 25):
            dotstring += self.dotstring[i:i+25] + s
        self.dotstring = dotstring

    def add_padding(self):
        padding = "."*self.display.w*self.display.h
        self.dotstring = padding + self.dotstring + padding

    def scroll(self):
        # self.add_spaces(spaces)
        # between letter spaces are now included in the font
        # cause this messed up the actual between words spaces
        self.add_padding()
        for offset in range(0, len(self.dotstring)-self.display.w*self.display.h, 5):
            for y in range(self.display.h):
                for x in range(self.display.w):
                    pixel = self.dotstring[x+y*self.display.w+offset]
                    if pixel == "X":
                        self.display.set_pixel(x, y, 'f'*6, False)
                    else:
                        self.display.set_pixel(x, y, '0'*6, False)
            sleep_us(100000)
            self.display.show()
