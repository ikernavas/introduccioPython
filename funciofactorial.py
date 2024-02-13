# Fes la funció factorial utilitzant un bucle for.

def factorial(n):
    if n < 0:
        return None  
    elif n == 0:
        return 1  
    else:
        resultat = 1
        for i in range(1, n + 1):
            resultat *= i
        return resultat


numero = 5
print(f"El factorial de {numero} és {factorial(numero)}")
