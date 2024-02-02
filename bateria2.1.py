# Programa que pregunta el nom de l'usuari i només dona la benvinguda si l'usuari es diu "Amilcar" o "Sila".

nom = input("Introdueix el teu nom: ")

if nom == "Amilcar" or nom == "Sila":
        print("Benvinguts al sistema, " + nom)
else:
        print("Accés denegat. Nom d'usuari no reconegut.")
