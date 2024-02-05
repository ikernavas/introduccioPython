# Programa que pregunta la nota a l'usuari i segons la nota diu el resultat obtingut: 1 a 4 - Insuficient, 5 - Suficient, 6 - Bé, 7 a 8 - Notable, 9 a 10 - Excel·lent.

nota = float(input("Diga'm la teva nota: "))
if nota >= 1 and nota <= 4:
    resultat = "Insuficient"
elif nota == 5:
    resultat = "Suficient"
elif nota == 6:
    resultat = "Bé"
elif nota >= 7 and nota <= 8:
    resultat = "Notable"
elif nota >= 9 and nota <= 10:
    resultat = "Excelent"
print "Tens un", resultat)
