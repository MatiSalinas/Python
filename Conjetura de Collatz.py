def secuencia(numero):
    global numero1
    if numero % 2 == 0:
        numero1 = numero / 2
    else:
        numero1 = (numero * 3) + 1

while True:
    try:
        print('Ingresa un numero entero')
        numero1 = int(input())
        break
    except ValueError:
        print('Que sea un numero entero porfavor')
        continue

while numero1 != 1:
    secuencia(numero1)
    print (int(numero1))



















