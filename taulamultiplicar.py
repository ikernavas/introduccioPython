# Fes un programa que pregunti un número i et tregui la seva taula de multiplicar.

numero = int(input("Introdueix un número: "))
print(f"Taula de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
