from machine import Pin, SPI
from display import Display
from text import Text
from utime import sleep_us
from urandom import randint
import _thread

def rand_color():
    return '%02x%02x%02x' % (randint(0, 254), randint(0, 254), randint(0, 254))

def main(program):
    spi = SPI(
        1,
        baudrate=2000000,
        polarity=0,
        phase=0,
        firstbit=SPI.MSB,
        mosi=Pin(16),
        sck=Pin(17)
    )

    color = rand_color()
    # For debugging
    #from dvd import main
    #main({"run": True, "display": { "height": 12, "width": 5}})

    height = program["display"]["height"]
    width = program["display"]["width"]
    d = Display(spi, height, width)
    dvd = [
        randint(0, width-1),  # x
        randint(0, height-1), # y
        #randint(-1, 1), # vx
        #randint(-1, 1)  # vy
        1,
        1
    ]
    lastX = 0
    lastY = 0
    while program["run"]:
        d.set_pixel(lastX, lastY, "0"*6)
        d.set_pixel(dvd[0], dvd[1], color)

        lastX = dvd[0]
        lastY = dvd[1]
        dvd[0] += dvd[2]
        dvd[1] += dvd[3]

        # check corners clock wise first, then sides
        if (dvd[0] == 0 and dvd[1] == 0 or 
              dvd[0] == width-1 and dvd[1] == 0 or
              dvd[0] == width-1 and dvd[1] == height-1 or
              dvd[0] == 0 and dvd[1] == height-1):
            dvd[2] *= -1
            dvd[3] *= -1
            # Epic moment when dvd hits corner
            color = rand_color()
        else:
            # sides except corners
            if dvd[0] == width-1 or dvd[0] == 0:
                dvd[2] *= -1
            elif dvd[1] == height-1 or dvd[1] == 0:
                dvd[3] *= -1

        # Decided against giving a parameter to the front end. It's OK like
        # this :)
        sleep_us(100000)


