>SPI2.setup({baud:1000000, mosi:D16, sck:D17 });
=undefined
>var lights = [0, 0, 255];
=[ 0, 0, 255 ]
>SPI2.send(lights);
=new Uint8Array([255, 255, 255])
    >SPI2.send([0,0,255]);
    =new Uint8Array([255, 255, 255])
    >SPI2.send([0,255,0]);
    =new Uint8Array([255, 255, 255])
    >SPI2.send([255,0,0]);
    =new Uint8Array([255, 255, 255])
    >SPI2.send([255,0,0, 0, 255, 0]);
    =new Uint8Array([255, 255, 255, 255, 255, 255])
    >SPI2.send([255,0,0, 0, 255, 0, 0, 0, 255]);
    =new Uint8Array([255, 255, 255, 255, 255, 255, 255, 255, 255])
    >SPI2.send([0,0,0, 0, 255, 0, 0, 0, 255]);
    =new Uint8Array([255, 255, 255, 255, 255, 255, 255, 255, 255])
    >SPI2.send([0,0,0, 0, 0, 0, 0, 0, 255]);
    =new Uint8Array([255, 255, 255, 255, 255, 255, 255, 255, 255])
