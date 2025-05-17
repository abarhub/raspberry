#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Mesure de la température et de l'humidité avec
un capteur DHT22 branché à un Rasbperry Pi.
Nécessite la bibliothèque d'Adafruit.
Pour plus d'infos:
https://electroniqueamateur.blogspot.com/2020/11/mesurer-la-temperature-et-lhumidite.html

branchement :
-broche + : entree 3V3
-broche out : GPIO 4
-broche + : ground GND

creation de l'environnement :
> python3 -m venv venv

ajout des dependances :
> sudo apt-get install python3-full
> sudo apt-get install libgpiod2
> venv/bin/pip3 install adafruit-blinka
> venv/bin/pip3 install adafruit-circuitpython-dht
> venv/bin/pip3 install RPi.GPIO


execution du programme :
> venv/bin/python3 test1.py

'''

import time
import board
import adafruit_dht
import math

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

while True:
    try:
        temperature = dhtDevice.temperature
        humidite = dhtDevice.humidity

        if temperature is None or humidite is None:
             print("pas de donne",temperature,humidite)
        else:
             # calcul du point de rosée  (formule de Heinrich Gustav Magnus-Tetens)
             alpha = math.log(humidite / 100.0) + (17.27 * temperature) / (237.3 + temperature)
             rosee = (237.3 * alpha) / (17.27 - alpha)

             #calcul de l'humidex
             humidex = temperature + 0.5555 * (6.11 * math.exp(5417.753 * (1 / 273.16 - 1 / (273.15 + rosee))) - 10)

             print("Temperature:  {:.1f} C    Humidite: {}%     Rosee:  {:.1f} C     Humidex:  {:.1f}"
                      .format(temperature , humidite, rosee , humidex))

    except RuntimeError as error:
        #print(error.args[0])
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
