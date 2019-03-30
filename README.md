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
spi = SPI(1, baudrate=2000000, polarity=0, phase=0, firstbit=SPI.MSB, mosi=Pin(16), sck=Pin(17))
# make the first led light up pink
spi.write(ubinascii.unhexlify(b'f141f4'))
```

## Useful links

- https://boneskull.com/micropython-on-esp32-part-1/
