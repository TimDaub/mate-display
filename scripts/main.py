import machine
import pixels
import array
import urandom
import time

# Source:
# https://github.com/FastLED/FastLED/blob/master/examples/Fire2012WithPalette/Fire2012WithPalette.ino

heatColors = array.array('L', [0x000000,
    0x330000, 0x660000, 0x990000, 0xCC0000, 0xFF0000,
    0xFF3300, 0xFF6600, 0xFF9900, 0xFFCC00, 0xFFFF00,
    0xFFFF33, 0xFFFF66, 0xFFFF99, 0xFFFFCC, 0xFFFFFF])


COOLING = 55
SPARKING = 120

l = pixels.Pixels(machine.Pin(15), 50, pixels.GRB)
cells = pixels.Array(len(l), 16)
vals = pixels.Array(len(l), 16)

while True:
    start = time.ticks_us()
    # Step 1.  Cool down every cell a little
    vals.random((((COOLING * 10) / len(l)) + 2) / 255.0)
    cells -= vals

    # Step 2.   Heat from each cell drifts 'up' and diffuses a little
    vals[:] = cells[:] # copy contents
    vals.itruediv(3)
    cells.fill(0)
    cells[1:] += vals
    cells[2:] += vals
    cells[2:] += vals

    # Step 3.   Randomly ignite new 'sparks' of heat near the bottom
    if urandom.getrandbits(8) < SPARKING:
        y = urandom.getrandbits(3)
        cells[y] = min(0.62, urandom.getrandbits(8)/255)

    # Step 4.   Map from heat cells to LED colors
    l.fill_palette_array(heatColors, cells, 0.25);

    l.write()
    stop = time.ticks_us()
    print('fps:', 1000000/(stop-start))
    time.sleep(0.10)
