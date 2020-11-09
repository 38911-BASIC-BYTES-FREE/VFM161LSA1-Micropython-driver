# VFM161LSA1-Micropython-driver

This is a micropython driver for the old fruit machine displays:
- VFM161LSA1
- M16LY03B
- 16LF01UA3
- PCB1613
- VAF169 
- PV0202-001-F
Tested with ESP8266 and ESP32.

Connection:

 GND---|12 11|---GND
/RST---|10 09|--- D0
 CLK---|08 07|--- NC
 NC ---|06 05|--- NC
 NC ---|04 03|--- NC
 VIN---|02 01|---VIN
 
 Connection for ESP8266:
 /RST -> PIN2
  CLK -> PIN14(SCK)
  D0  -> PIN13(MOSI)
  GND -> GND
  VIN -> External power supply, do not connect to +5V od the ESP.
  
 VIN depends on the type of display. Please refer to the datasheet. For some of displays it requires +12V and +5V.
 
Usage example:

import VFD_driver
from utime import sleep_ms

display = VFD_driver.VMF161(1, 2, brightness=15)

display.clear()
display.text('Sample text')

