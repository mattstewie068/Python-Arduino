import time
import pyfirmata

uno = pyfirmata.Arduino('COM5')

wled = uno.get_pin('d:10:o')
rled = uno.get_pin('d:9:o')
yled = uno.get_pin('d:8:o')
gled = uno.get_pin('d:7:o')

while True:
    yled.write(1)
    time.sleep(1)
    yled.write(0)
    time.sleep(1)
