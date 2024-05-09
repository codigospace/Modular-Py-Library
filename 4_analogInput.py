import Modular
import time
adc = Modular.analogInput(3)
try:
	adc.init()
	while 1:
		print(adc.read())
		time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()
