from gpiozero import Button,LED
from time import sleep

dureeJaune=5
dureeTemporisation=15

button = Button(23)	

ledVert = LED(17)
ledJaune = LED(27)
ledRouge = LED(22)

def temporisation(ledDepart,ledJaune,letTemporisation,dureeJaune,dureeTemporisation):

	ledDepart.on()

	while True:
		button.wait_for_press()
		ledDepart.off()
		ledJaune.on()
		sleep(dureeJaune)
		ledJaune.off()
		letTemporisation.on()
		sleep(dureeTemporisation)
		letTemporisation.off()
		ledDepart.on()


def arret(ledVert,ledJaune,ledRouge):
	ledVert.off()
	ledJaune.off()
	ledRouge.off()


temporisation(ledVert,ledJaune,ledRouge,dureeJaune,dureeTemporisation)


arret(ledVert,ledJaune,ledRouge)
