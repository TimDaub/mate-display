To flash Espruino on the ESP32, use the following command:

```bash
esptool.py --chip esp32 --port "/dev/tty.SLAB_USBtoUART" --baud 921600 \
    write_flash -z --flash_mode "dio" --flash_freq "40m" 0x1000 1.bin \
    0x10000 2.bin 0x8000 3.bin
```

The firmware is uploaded in this directory (1.bin, 2.bin, 3.bin). Make sure
to change the `--port` depending on your OS.
