# Fes un programa que imprimeixi per pantalla els números primers.

def es_primer(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

limit = int(input("Introdueix el límit superior: "))
print("Els números primers fins a", limit, "són:")
for num in range(2, limit + 1):
    if es_primer(num):
        print(num, end=" ")
