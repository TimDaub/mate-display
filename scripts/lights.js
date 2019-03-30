var nrOfPixels = 50;
var rgb = new Uint8Array(nrOfPixels*3);

var k=0,jj=0;

SPI2.setup({baud:1000000, mosi:B34, sck:B35 }); 
USB.setup({baudrate:115200});
var serialBuffer = createRingBuffer(3);

function sendDataOut() {
  SPI2.send(rgb);
}


setInterval(function() {
    jj=k;
    for (var i=0;i<rgb.length;i+=3) {
      wheel(i, k++);
    }
    k=(jj+1)%255;
    sendDataOut();
  //}
}, 15);

console.log("init done");
            
Pin.prototype.startFlashing = function(period) {
  var me = this;
  var on = false;
  setInterval(function() {
    on = !on;
    digitalWrite(me, on);
  }, period);
};
LED3.startFlashing(500);

function wheel(ofs, pos) {
  pos %= 255;
  if (pos < 86) {
    Color(ofs, pos * 3, 255 - pos * 3, 0);
  } 
  else if (pos < 171) {
    pos -= 85;
    Color(ofs, 255 - pos * 3, 0, pos * 3);
  } 
  else {
    pos -= 170; 
    Color(ofs, 0, pos * 3, 255 - pos * 3);
  }
}

function Color(ofs, r,g,b) {
  rgb[ofs] = r%255;
  rgb[ofs+1] = g%255;
  rgb[ofs+2] = b%255;
}
