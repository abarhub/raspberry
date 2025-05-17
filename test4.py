from gpiozero import Button,LED
from time import sleep

dureeJaune=5
dureeTemporisation=15

button = Button(23)	

ledVert = LED(17)
ledJaune = LED(27)
ledRouge = LED(22)

ledVert2 = LED(24)
ledJaune2 = LED(8)
ledRouge2 = LED(25)


class Feux:
	def __init__(self, ledVert, ledJaune,ledRouge):
		self.ledVert = ledVert
		self.ledJaune = ledJaune
		self.ledRouge = ledRouge
	
	def setVert(self):
		self.ledVert.on()
		self.ledJaune.off()
		self.ledRouge.off()
	
	def setJaune(self):
		self.ledVert.off()
		self.ledJaune.on()
		self.ledRouge.off()
		
	
	def setRouge(self):
		self.ledVert.off()
		self.ledJaune.off()
		self.ledRouge.on()
		
	def setArret(self):
		self.ledVert.off()
		self.ledJaune.off()
		self.ledRouge.off()
		
	

feux1=Feux(ledVert,ledJaune,ledRouge)
feux2=Feux(ledVert2,ledJaune2,ledRouge2)

def temporisation0(ledDepart,ledJaune,ledTemporisation,dureeJaune,dureeTemporisation,ledVert2,ledJaune2,ledRouge2):

	ledDepart.on()
	ledJaune.off()
	ledTemporisation.off()
	
	ledVert2.off()
	ledJaune2.off()
	ledRouge2.on()

	while True:
		button.wait_for_press()
		ledDepart.off()
		ledJaune.on()
		sleep(dureeJaune)
		ledJaune.off()
		ledTemporisation.on()
		ledVert2.on()
		ledRouge2.off()
		sleep(dureeTemporisation)	
		ledVert2.off()
		ledJaune2.on()
		ledRouge2.off()
		sleep(dureeJaune)
		ledTemporisation.off()
		ledDepart.on()	
		ledVert2.off()
		ledJaune2.off()
		ledRouge2.on()


def temporisation(feux1,feux2,dureeJaune,dureeTemporisation):

	feux1.setVert()
	
	feux2.setRouge()

	while True:
		button.wait_for_press()
		feux1.setJaune()
		sleep(dureeJaune)
		feux1.setRouge()
		feux2.setVert()
		sleep(dureeTemporisation)	
		feux2.setJaune()
		sleep(dureeJaune)
		feux2.setRouge()
		feux1.setVert()


def arret(ledVert,ledJaune,ledRouge):
	ledVert.off()
	ledJaune.off()
	ledRouge.off()


temporisation(feux1,feux2,dureeJaune,dureeTemporisation)


#arret(ledVert,ledJaune,ledRouge)

#arret(ledVert2,ledJaune2,ledRouge2)

feux1.setArret()

feux2.setArret()


