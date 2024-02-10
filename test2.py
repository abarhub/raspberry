from gpiozero import LED,Button
from signal import pause

rouge=LED(23)
bouton=Button(24)

print("Appuyez sur le bouton pou allumer la LED")

rouge.source=bouton

pause()

