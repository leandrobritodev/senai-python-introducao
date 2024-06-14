import keyboard
import mouse

macro = ''

while True:
    if mouse.is_pressed(button='middle'):
        keyboard.write('Abacabb', delay=0.1)
    elif mouse.is_pressed(button='right'):
        break