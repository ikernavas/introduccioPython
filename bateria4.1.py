# Fes un programa que pregunta un número i et retorna tots els números que són divisors del número (els que la seva divisió no té residu).

numero = int(input("Diga'm un numero: "))
for i in range (1,numero+1):
    if numero % i == 0:
        print(i)
