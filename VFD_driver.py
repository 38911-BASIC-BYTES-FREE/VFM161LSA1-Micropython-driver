from machine import SPI, Pin
import utime

reset = Pin(2, Pin.OUT)
spi = SPI(1, baudrate=1000000, polarity=1, phase=0)
spi.init(baudrate=1000000)

reset.off()
utime.sleep_us(100)
reset.on()
a = bytearray(1)
a[0] = 0b11000000 #16 digits
spi.write(a)
#utime.sleep_us(100)
a[0] = 0b11111111 #brightness 100%. For 50%: 11111010
spi.write(a)
#utime.sleep_us(100)
a[0] = 0b10101111 #cursor home
spi.write(a)
#utime.sleep_us(100)

a[0] = 0b00000000

napis = "* BCDEFGHIJKLMN*"
for i in range (0,16):
  a[0] = ord(napis[i:i+1])
  spi.write(a)
  #utime.sleep_us(100)



