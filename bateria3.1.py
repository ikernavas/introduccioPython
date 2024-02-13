# Fes un programa que demana un número a l'usuari i imprimeix la seva taula de multiplicar (del 1 al 10).

numero = int(input("Introdueix un número: "))
print(f"Taula de multiplicar del {numero}:")
for i in range(1, 11):
    print("{numero} x {i} = {numero * i}")
