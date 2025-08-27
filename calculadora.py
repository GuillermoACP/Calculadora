import math

def suma(a,b):
    return a + b

def raiz_cuadrada(a):
    return math.sqrt(a)

def pedir_numeros():
    while True:
        try:
            a = float(input('Numero A: '))
            b = float(input('Numero B: '))
            return a, b
        except ValueError:
            print('Ingrese solo números válidos')

def pedir_raiz():
    while True:
        try:
            x = float(input('Numero: '))
            if x < 0:
                print("No se puede sacar raíz cuadrada de un número negativo")
                continue
            return x
        except ValueError:
            print('Ingrese solo números válidos')


def menu():
    while True:
        print('MENU')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        print('5. Exponencial')
        print('6. Raiz Cuadra')
        print('0. Salir')

        opcion = input('Opcion: ')


        if opcion == '0':
            break
        elif opcion == '1':
            a, b = pedir_numeros()
            print (f'{a} + {b} = {suma(a, b)}')
            input("Presiona ENTER para volver al menú...")
        elif opcion == '6':
            a = pedir_raiz()
            print(f'√ {a} = {raiz_cuadrada(a)}')
            input("Presiona ENTER para volver al menú...")
        else:
            print('Numero invalido')


             



menu()
