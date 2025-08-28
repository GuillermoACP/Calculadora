import math

def menu():
    print('MENU')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Exponencial')
    print('6. Raiz Cuadra')
    print('7. Areas (submenu)')
    print('0. Salir')

def menu_areas():
    print('=== MENU AREAS===')
    print('1. Cuadrado')

def entrada():
    while True:
        valor = input('Ingresa numero o = para salir: ')
        if valor == '=':
            return None
        try:
            return float(valor)
        except ValueError:
            print("Entrada no valida.")

def mostrar_resultado(resultado):
    """
    Muestra el resultado final si existe y espera a que el usuario presione ENTER.
    """
    if resultado is not None:
        print(f"Resultado final: {resultado}")
        input("Presiona ENTER para volver al menú...")

           
def suma():
    resultado = None
    while True:
        numero = entrada()
        if numero is None: 
            break

        if resultado is None: 
            resultado = numero
            print(f"Total = {resultado}")
        else:
            print(f"{resultado} + {numero} = {resultado + numero}")
            resultado = resultado + numero

    mostrar_resultado(resultado)
    return resultado


def resta():
    resultado = None
    while True:
        numero = entrada()
        if numero is None:
            break

        if resultado is None:
            resultado = numero
            print(f"Total = {resultado}")
        else:
            print(f"{resultado} - {numero} = {resultado - numero}")
            resultado = resultado - numero


    mostrar_resultado(resultado)
    return resultado

def multiplicacion():
    resultado = None
    while True:
        numero = entrada()
        if numero is None:
            break

        if resultado is None:
            resultado = numero
            print(f"Total = {resultado}")
        else:
            print(f"{resultado} * {numero} = {resultado * numero}")
            resultado = resultado * numero
    
    mostrar_resultado(resultado)
    return resultado

def division():
    resultado = None
    while True:
        numero = entrada()
        if numero is None:
            break

        if resultado is None:
            resultado = numero
            print(f"Total = {resultado}")
        else:
            print(f"{resultado} / {numero} = {resultado / numero}")
            resultado = resultado / numero
    
    mostrar_resultado(resultado)
    return resultado

def exponencial():
    resultado = None
    while True:
        numero = entrada()
        if numero is None:
            break

        if resultado is None:
            resultado = numero
            print(f"Total = {resultado}")
        else:
            print(f"{resultado} ^ {numero} = {resultado ** numero}")
            resultado = resultado ** numero
    
    mostrar_resultado(resultado)
    return resultado

def raiz_cuadrada():
    while True:
        entrada = input('Ingresa un numero o = para salir: ')
        if entrada == '=':
            break
        try:
            numero = float(entrada)
            if numero < 0:
                print('Error: No se puede obtener raiz de un negativo.')
                continue
            raiz = math.sqrt(numero)
            print(f"√{numero} = {raiz}")
        except:
            print ('Entrada no valida.')            
