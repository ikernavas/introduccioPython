# - Programa que pregunta un número a l'usuari i diu si és major o menor que 100.

numero_usuari = float(input("Si us plau, introdueix un número: "))
if numero_usuari > 100:
    print("El número introduit es major que 100.")
elif numero_usuari < 100:
    print("El numero introduit es menor que 100.")
else:
    print("El numero introduit es igual a 100.")
