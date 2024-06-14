import keyboard
import mouse
import time
import csv

macro = ''
ativar = False
while True:
    if keyboard.is_pressed("Ctrl"):
        macro = mouse.record()
        # keyboard.write('Abacabb', delay=0.1)
    if macro != '':
        if keyboard.is_pressed("Ctrl"):
            ativar = not ativar
            time.sleep(0.5)
