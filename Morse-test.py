import machine
import utime
# test-run of Morse code message
led_pin = machine.Pin(25, machine.Pin.OUT)

for i in range(1, 4):
    led_pin.value(1)
    utime.sleep(0.5)
    led_pin.value(0)
    utime.sleep(0.5)

for i in range(1, 4):
    led_pin.value(1)
    utime.sleep(3)
    led_pin.value(0)
    utime.sleep(0.5)
    
for i in range(1, 4):
    led_pin.value(1)
    utime.sleep(0.5)
    led_pin.value(0)
    utime.sleep(0.5)
