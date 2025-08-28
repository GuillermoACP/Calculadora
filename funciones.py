import math

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
    resultado = None
    while True:
        entrada = input('Ingresa numero o = para sumar: ')
        if entrada == '=':
            break
        try:
            numero = float(entrada)
            if resultado is None: 
                resultado = numero
                print(f"Total = {resultado}")
            else:
                print(f"{resultado} + {numero} = {resultado + numero}")
                resultado += numero
        except ValueError:
            print('Entrada no valida.')

    if resultado is not None:
        print(f"Resultado final: {resultado}")
        input("Presiona ENTER para volver al menú...")
    return resultado


def resta_varios():
    resultado = None
    while True:
        entrada = input('Ingresa un numero o = para restar: ')
        if entrada == '=':
            break
        try:
            numero = float(entrada)
            if resultado is None:
                resultado = numero
                print(f"Total = {resultado}")
            else:
                print(f"{resultado} - {numero} = {resultado - numero}")
                resultado -= numero
        except ValueError:
            print("Entrada no valida.")

    if resultado is not None:
        print(f"Resultado final: {resultado}")
        input("Presiona ENTER para volver al menú...")
    return resultado
        
