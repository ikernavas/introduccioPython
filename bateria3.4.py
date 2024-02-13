# Modifica el programa anterior per que sigui l'usuari si vol sumar els números parells o els senars.

def suma_numeros_fins_a(numero, parells=True):
    suma = 0
    for i in range(1 if not parells else 2, numero + 1, 2 if not parells else 1):
        suma += i
    print(f"La suma dels {'senars' if not parells else 'parells'} fins a {numero} és: {suma}")

numero = int(input("Introdueix un número: "))
opcio = input("Vols sumar els números parells? (sí/no): ").lower()
suma_numeros_fins_a(numero, parells=(opcio == "sí" or opcio == "si"))
