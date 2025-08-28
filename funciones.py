import math

def pedir_numeros(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return float(entrada)
        except ValueError:
            print('Entrada no valida.')

def menu():
    print('MENU')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Exponencial')
    print('6. Raiz Cuadra')
    print('0. Salir')
           
def suma_varios():
    numeros = []
    while True:
        entrada = input('Ingresa un numero o = ')
        if entrada == '=':
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print('Entrada no valida.')
    return sum(numeros)

def raiz_cuadrada(a):
    return math.sqrt(a)


