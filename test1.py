import gpiozero

position=gpiozero.Button(24)

while True:
        if position.is_pressed:
                print("Le bouton est presse")
        else:
                print("Le bouton est relache")

