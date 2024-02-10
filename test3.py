from gpiozero import Button,LED
from time import sleep

button = Button(23)	

ledVert = LED(17)
ledJaune = LED(27)
ledRouge = LED(22)


ledRouge.on()

while True:
	button.wait_for_press()
	ledRouge.off()
	ledJaune.on()
	sleep(5)
	ledJaune.off()
	ledVert.on()
	sleep(30)
	ledVert.off()
	ledRouge.on()


ledRouge.off()

