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

## Useful links

- https://boneskull.com/micropython-on-esp32-part-1/
