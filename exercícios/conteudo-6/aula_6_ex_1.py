import keyboard

texto = ''
while True:
    evento = keyboard.read_event()
    if evento.event_type == keyboard.KEY_DOWN:
        letra = evento.name
        if len(letra) == 1:
            texto += letra
        if letra == 'backspace':
            texto = texto[:-1]
        if len(texto) == 3:
            if texto == 'ola':
                keyboard.write(' mundo')
            texto = ''
        print(f'Texto: {texto}')