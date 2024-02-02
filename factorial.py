# Feu un programa que pregunti un número a l'usuari i retorni el valor factorial d'aquell número.

fact = int(input("Introdueix un numero per fer el factorial: "))
resultat = 1
fact_inicial = fact
while fact >0:
        Resultat = resultat * fact
        fact -= 1
        print("Resultat: ",resultat)
        print("Fact: ",fact)

print("El factorial del numero ", fact_inicial, "es ", resultat)
