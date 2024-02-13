# Modifica el programa anterior per a que només sumi els números parells.

def suma_parells_fins_a(numero):
    suma = 0
    for i in range(2, numero + 1, 2):  # Comença en 2 i salta de 2 en 2 fins a numero
        suma += i
    print("La suma dels números parells fins a {numero} és: {suma}")

numero = int(input("Introdueix un número: "))
suma_parells_fins_a(numero)
