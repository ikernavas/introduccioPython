# Fes un programa que pregunta valors de números sencers a l'usuari i els guarda en una llista fins que l'usuari introdueix la paraula final, i després torna la suma de tots els números introduïts.

suma_total = 0

while True:
    entrada = input("Introdueix un número enter (o 'final' per acabar): ")
    if entrada == 'final':
        break  
    try:
        suma_total += int(entrada)  
    except ValueError:
        print("Error: Si us plau, introdueix un número enter o 'final'.")

print("La suma de tots els números introduïts és:", suma_total)
