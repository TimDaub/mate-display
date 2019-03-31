# Mate Display

## Useful commands

To erase the chip's memory

```bash
esptool.py --chip esp32 -p /dev/tty.SLAB_USBtoUART erase_flash
```

To flash micropython

```bash
esptool.py --chip esp32 -p /dev/tty.SLAB_USBtoUART write_flash \
  -z 0x1000 ../../Downloads/esp32-20190329-v1.10-245-g1a608ce1e.bin
```

To run the REPL console on the chip

```bash
screen /dev/tty.SLAB_USBtoUART 115200
```

## SPI with micropython REPL

```python
from machine import Pin, SPI
import ubinascii
spi = SPI(1, baudrate=2000000, polarity=0, phase=0, firstbit=SPI.MSB, mosi=Pin(16), sck=Pin(17))
# make the first led light up pink
spi.write(ubinascii.unhexlify(b'f141f4'))
```

```python
# make leds blink randomly
def randhex():
  return str(random.choice("0123456789ABCDEF")) + str(random.choice("015D23456789ABCDEF"))
  
def rand():
  return "".join([randhex() for i in range(3)])

while(True):
  data = '000000'*50
  num = random.randint(0,6*50-6)
  data = data[:num] + rand() + data[num+6:]
  spi.write(ubinascii.unhexlify(data))
```

```python
# ascending light
import utime
color = "f141f4"
color = "f141f4"
while(True):
  data = "000000"*50
  for i in range(0, 50):
    data = color*i + data[i*6:len(data)]
    utime.sleep_us(1000)
    spi.write(ubinascii.unhexlify(data))
```

```python
# flash strip
color = "f141f4"
one = color*50
two = '000000'*50
switch = True
while(True):
  if switch:
    spi.write(ubinascii.unhexlify(one))
  else:
    spi.write(ubinascii.unhexlify(two))
  switch = not switch
```

## Usage with Pixels

```python
while(True):
  for i in range(0, 20):
    p.set_pixel(i, color)
    p.show()
    sleep_us(200000)
  p.clear()
  sleep_us(200000)
```

## Tips

- Don't use while loops in any .py file. You'll have to reflash the esp32 as you will not be able to write files to it anymore. It's busy executing the while loop.

## Useful links

- https://boneskull.com/micropython-on-esp32-part-1/
