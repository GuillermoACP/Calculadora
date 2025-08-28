from funciones import *

def calculadora():
    resultado = None

    while True:
        menu()
        opcion = input('Opcion: ')


        if opcion == '0':
            break
        elif opcion == '1':
            resultado = suma_varios()

        else:
            print('Numero invalido')
            continue
        
        if resultado is not None:
            print(resultado)
            input("Presiona ENTER para volver al menú...")



             



calculadora()
