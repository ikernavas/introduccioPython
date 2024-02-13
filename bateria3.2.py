# Fes un programa que pregunti un número a l'usuari i retorni la suma de tots els números fins el que ha introduït l'usuari.

def suma_fins_a(numero):
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    print(f"La suma de tots els nombres fins a {numero} és: {suma}")

numero = int(input("Introdueix un número: "))
suma_fins_a(numero)
