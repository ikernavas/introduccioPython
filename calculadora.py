# Calculadora

print("Benvinguts a pycalc, introduiu una de les següents opcions:")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")

while True:
    operacio = input("Inserteu Operació(1/2/3/4): ")
    if operacio in ('1', '2', '3', '4'):
        x = float(input("Entra un número: "))
        y = float(input("Entra un segon número: "))

        suma = float(x + y)
        resta = float(x - y)
        multiplicacio = float(x * y)
        divisio = float(x / y)

        if operacio == ("1"):
            print("suma" "= ", suma)

        elif operacio == ("2"):
            print("resta = ", resta)

        elif operacio == ("3"):
            print("multiplicacio = ", multiplicacio)

        elif operacio == ("4"):
            print("divisio = ", divisio)

        seguent_operació = input("Seguent operació? (y/n): ")
        if seguent_operació == "n":
            break

    else:
        print("Entrada invalida")
