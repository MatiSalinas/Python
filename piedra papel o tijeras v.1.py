from operator import truediv
import random, sys
ganadas = 0
perdidas = 0
empates = 0

while True:
    print('Ganaste: %d , Perdiste: %d, y Empataste: %d'%(ganadas,perdidas,empates))
    print('Pone (r)ock, (p)aper, (s)cissors o q para salir')
    
    
    while True:
        eleccion = input()
        if eleccion == 'q':
            sys.exit()
        if eleccion == 'p':
            print ('elegiste papel....\nCONTRA...')
            break
        elif eleccion == 'r':
            print ('elegiste piedra....\nCONTRA...')
            break
        elif eleccion == 's':
            print ('elegiste tijeras....\nCONTRA...')
            break
        else:
            continue
    iaEleccion = random.randint(1,3)
    if iaEleccion == 1:
        iaEleccion ='r'
        print('PIEDRA!!!!')
    elif iaEleccion == 2:
        iaEleccion ='p'
        print('PAPEL!!!!')
    elif iaEleccion == 3:
        iaEleccion ='s'
        print('TIJERAS!!!!')
    # 1 == r , 2 == p, 3==s
    if eleccion == iaEleccion:
        print('fue un empate')
        empates = empates + 1
    elif eleccion == 'r' and iaEleccion == 'p' :
        print ('PIEDRA PIERDE CONTRA PAPEL , PERDISTE.')
        perdidas = perdidas + 1
    elif eleccion == 'r' and iaEleccion =='s':
        print ('PIEDRAS LE GANA A TIJERAS, GANASTE')
        ganadas = ganadas + 1
    elif eleccion == 'p' and iaEleccion == 's' :
        print ('PAPEL PIERDE CONTRA PIEDRA, PERDISTE.')
        perdidas = perdidas + 1
    elif eleccion=='p' and iaEleccion =='r':
        print('PAPEL LE GANA A PIEDRA, GANASTE.')
        ganadas = ganadas + 1
    elif eleccion == 's' and iaEleccion == 'p':
        print ('TIJERAS LE GANA A PAPEL, GANASTE')
        ganadas = ganadas + 1
    elif eleccion == 's' and iaEleccion == 'r':
        print('TIJERAS PIERDE CONTRA PIEDRA, PERDISTE.')
        perdidas = perdidas + 1


















