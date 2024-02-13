#Fes un programa que pregunti un número i sumi els números imparells entre 1 i el número introduït.

def suma_imparells_fins_a(num):
    return sum(range(1, num + 1, 2))

numero = int(input("Introdueix un número: "))
resultat = suma_imparells_fins_a(numero)
print(f"La suma dels números imparells fins a {numero} és: {resultat}")
