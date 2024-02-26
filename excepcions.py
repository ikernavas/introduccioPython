# Activitat 1: Pregunta a l'usuari dos nombres i divideix-los. Utilitza un block try i except per evitar l'error de divisio per zero

try:

    num1 = float(input("Introdueix el primer nombre: "))
    num2 = float(input("Introdueix el segon nombre: "))

    resultat = num1 / num2

    print("El resultat de la divisió és:", resultat)

except:
    print("S'ha produit un error.")


# Activitat 2: Demana a l'usuari que introdueixi un número, i intenta convertir aquesta entrada en un enter. Utilitza try i except per capturar qualsevol error de conversió.

try:

    entrada = input("Introdueix un número: ")

    numero = int(entrada)

    print("El numero convertit és:", numero)

except:
    print("S'ha produit un error en la conversio del nom")

# Activitat 3: Pregunta a l'usuari dos valors i intenta sumar-los. Utilitza try i except per capturar errors quan els valors no són números.

try:
    valor1 = float(input("Introdueix el primer valor: "))
    valor2 = float(input("Introdueix un altre valor: "))

    resultat = valor1 + valor2

    print("La suma dels dos valors es:", resultat)

except:
    print("Error: Un o tots dels valors no son valids.")

# Activitat 4: Crea una llista amb alguns elements i demana a l'usuari un índex. Utilitza try i except per gestionar l'error que es produeix quan l'índex no existeix a la llista.

