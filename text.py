import json

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

    def set_letter(self, index):
        dotstring = self.encode()
        denominator = 25
        letters = [dotstring[i:i+denominator]
                    for i in range(0, len(dotstring), denominator)]
        letter = letters[index]
        col = 0
        row = 0
        for pixel in letter:
            if col == self.display.w:
                row += 1
                col = 0
            if pixel == "X":
                self.display.set_pixel(col, row, 'f'*6)
            else:
                self.display.set_pixel(col, row, '0'*6)
            col += 1

    def offset(self, dx, dy):
        for x in range(0, self.display.h):
            for y in range(0, self.display.w):
                color = self.display.get_color(x, y) or '0'*6
                self.display.set_pixel(x+dx, y+dy, color)
                 
