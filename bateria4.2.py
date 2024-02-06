#Fes un programa que pregunti números a l'usuari i calculi la seva mitjana, el programa preguntarà números fins que l'usuari escrigui un 0.

resultat = 0
suma_numeros = 0
quantitat_numeros = 0
while True:
    num = int(input("Digues un numero: "))
    if num == 0:
        break
    quantitat_numeros += 1
    suma_numeros += num
resultat = suma_numeros / quantitat_numeros
print(resultat)
