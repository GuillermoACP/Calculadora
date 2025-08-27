def suma(a,b):
    return a + b

def pedir_numero():
    while True:
        try:
            a = float(input('Numero A: '))
            b = float(input('Numero B: '))
            return a, b
        except ValueError:
            print('Ingrese solo números válidos')


def menu():
    while True:
        print('MENU')
        print('1. Suma')

        opcion = input('Opcion: ')


        if opcion == '0':
            break
        elif opcion == '1':
            a, b = pedir_numero()
            print (suma(a, b))
        else:
            print('Numero invalido')


             



menu()
