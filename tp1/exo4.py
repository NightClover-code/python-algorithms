a = int(input('Entrez le premier nombre: '))
b = int(input('Entrez le deuxieme nombre: '))

if (a >=0 and b >= 0):
    if (a == 0 or b == 0):
        print('Nul')
    else:
        print('Positif')
elif (a < 0 and b < 0):
    print('Positif')
else:
    print('Negatif')