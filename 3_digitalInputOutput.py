import Modular
import time
led = Modular.digitalOutput(1)
but = Modular.digitalInput(0)
try:
	led.init()
	but.init()
	while 1:
		if but.read():
			led.write(HIGH)
		else:
			led.write(LOW)
except KeyboardInterrupt:
	GPIO.cleanup()
