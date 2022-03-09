from re import T
import sys, time

identacion = 0

creciendo = True

while True:
    try:
        print(' ' * identacion, end='')
        print('******')
        time.sleep(0.1) # detiene el programa 0.1 segundos

        if creciendo:
            identacion = identacion + 1 # se van aumentando los espacios
            if identacion == 20:
                creciendo = False # se cambia la direccion
        else:
            identacion = identacion - 1
            if identacion == 0:
                creciendo = True
    except KeyboardInterrupt: # si se presiona Ctrl + c se interrumpe
        sys.exit()














