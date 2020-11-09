import VFD_driver
from utime import sleep_ms

display = VFD_driver.VMF161(1, 2, brightness=15)

display.clear()
display.text('Sample text')
  
