from funciones import *

def calculadora():

    while True:
        menu()
        opcion = input('Opcion: ')


        if opcion == '0':
            break
        elif opcion == '1':
            resultado = suma()

        elif opcion == '2':
            resultado = resta()

        elif opcion == '3':
            resultado = multiplicacion()

        elif opcion == '4':
            resultado = division()

        elif opcion == '5':
            resultado = exponencial()

        elif opcion == '6':
            resultado = raiz_cuadrada()

        elif opcion == '7':
            while True:
                menu_areas()
                opcion_areas = input('Opcion: ')

                if opcion_areas == '0':
                    menu()

                elif opcion_areas == '1':
                    resultado = area_cuadrado()

                else:
                    print('Numero invalido')
                    continue

        else:
            print('Numero invalido')
            continue
        




             



calculadora()
