from funciones import *

def calculadora():

    while True:
        menu()
        opcion = input('Opcion: ')


        if opcion == '0':
            break
        elif opcion == '1':
            resultado = suma_varios()
        elif opcion == '2':
            resultado = resta_varios()
        elif opcion == '6':
            resultado = raiz_cuadrada()

        else:
            print('Numero invalido')
            continue
        




             



calculadora()
