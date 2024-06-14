import keyboard
import mouse

eventos = ''
while True:
    if keyboard.is_pressed("Ctrl"):
        mouse.drag(0, 0, 0, 100, absolute=False, duration=0.1)
        mouse.drag(0, 0, 50, 0, absolute=False, duration=0.1)
        # eventos = mouse.get_position()
    elif keyboard.is_pressed("Shift"):
        break
