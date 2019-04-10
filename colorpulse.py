from machine import Pin, SPI
from display import Display
from pixels import Pixels
from utime import sleep_us

r = 255
g = 0
b = 0

def main(program):
    distance = int(program["distance"])
    steps = int(program["steps"])
    # steps has to be a divisor of 255
    global r
    global b
    global g
    r = 255
    g = 0
    b = 0
    pattern = [0, 1, 2, 3, 4,
               4, 3, 2, 1, 1,
               2, 2, 3, 4, 5,
               5, 5, 4, 3, 3,
               4, 4, 5, 5, 6,
               6, 6, 5, 5, 4,
               5, 5, 6, 6, 7,
               7, 7, 6, 6, 6,
               6, 6, 7, 7, 8,
               8, 8, 7, 7, 7,
               7, 8, 8, 8, 9,
               9, 9, 8, 8, 8]

    spi = SPI(
        1,
        baudrate=2000000,
        polarity=0,
        phase=0,
        firstbit=SPI.MSB,
        mosi=Pin(16),
        sck=Pin(17)
    )
    d = Display(spi, program["display"]["height"], program["display"]["width"])
    colors = []
    while program["run"]:
        if not colors:
            for i in range(0, (max(pattern)+1)):
                # init fill
                colorflow = []
                for n in range(0, distance):
                    colorflow.insert(n, colorsetter(steps))
                colors.insert(0, colorflow)
        else:
            colorflow = []
            for n in range(0, distance):
                colorflow.insert(n, colorsetter(steps))
            colors.insert(0, colorflow)
        colors = colors[0:(max(pattern)+1)]
        for i in range(0, distance):
            display = ""
            for n in range(0, len(pattern)):
                display += colors[pattern[n]][i]
                d.set_data(display)
                d.show()
        #sleep_us(1000000)
    d.clear()

def rgb2hex(r, g, b):
    return '%02x%02x%02x' % (r, g, b)

def colorsetter(steps):
    global r
    global g
    global b
    #steps has to be a divisor of 255
    if r == 255 and g == 0 and b < 255:
        # adding blue
        b += steps
        return rgb2hex(r, g, b)

    if r > 0 and g == 0 and b == 255:
        # subtracting red
        r -= steps
        return rgb2hex(r, g, b)

    if r == 0 and g < 255 and b == 255:
        # adding green
        g += steps
        return rgb2hex(r, g, b)

    if r == 0 and g == 255 and b > 0:
        # subtracting blue
        b -= steps
        return rgb2hex(r, g, b)

    if r < 255 and g == 255 and b == 0:
        # adding red
        r += steps
        return rgb2hex(r, g, b)

    if r == 255 and g > 0 and b == 0:
        # subtracting green
        g -= steps
        return rgb2hex(r, g, b)
