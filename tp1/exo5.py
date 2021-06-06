note = int(input("Entrez votre note: "))

if (16 <= note <= 20):
    print('T.Bien')
elif (14 <= note < 16):
    print('Bien')
elif (12 <= note < 14):
    print('A.Bien')
elif (10 <= note < 12):
    print('Passable')
elif (note < 10):
    print('Redoublant')
else:
    print('Erreur de sasie')

