"""exos TP1 initialement séparés dans plusieurs fichiers 
et fusionnés dans celui ci pour l'envoi dans la plateforme moodle"""

# exo1
#############################################

tva = 0.2

prixHT = float(input("Entrez le prix HT de l'articles: "))
nb = int(input("Entrez le nombre d'articles: "))

ttc = prixHT + (prixHT * tva)

print("Le prix ttc de l'article est: ", ttc, f"le prix ttc de {nb} articles est: ", ttc * nb)


#exo2
#############################################


seconds = int(input('Entrez le nombre de secondes: '))

hours, seconds =  divmod(seconds, 3600)

minutes, seconds = divmod(seconds, 60)

print(hours, 'h', minutes, 'm', seconds, 's')

#exo3
#############################################


random_num = int(input("Entrez un entier: "))

if (random_num % 2) == 0:
    print('Le nombre est pair')
else:
    print('Le nombre est impair')

#exo4
#############################################


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

#exo5
#############################################

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

#exo6
#############################################

a = int(input('Entrez un nombre a: '))
b = int(input('Entrez un nombre b: '))
op = input('Entrez un opérateur. Choix possibles: +, *, /, - \n')

printMsg = 'le résultat est: '

if (op == '+'):
    print(printMsg, a + b)
elif (op == '*'):
    print(printMsg, a * b)
elif (op == '/'):
    print(printMsg, a / b)
elif (op == '-'):
    print(printMsg, a - b)
else: 
    print('Opérateur erroné')
    
#exo7
#############################################

import math

def solve_equation(a, b, c):
    x = 0
    if (a != 0):
        delta = b**2 - 4*a*c
        if (delta >= 0):
            if (delta == 0):
                x = -b/2*a
                return x
            else:
                return (-b - math.sqrt(delta) / 2*a, -b + math.sqrt(delta) / 2*a)
        else:
            return 'pas de solution'
    else:
        if (b == 0):
            if (c == 0):
                return 'tout entier est solution'
            else:
                return 'pas de solution'
        else:
            x = -c/b
            return x



a = int(input('Entrez la valeur de a: '))
b = int(input('Entrez la valeur de b: '))
c = int(input('Entrez la valeur de c: '))

print(f'La solution de {a}x² + {b}x + {c} = 0 est: ', solve_equation(a, b, c))


#exo8
#############################################

n = int(input("Entrez un nombre de 3 chiffres: "))

while len(str(n)) != 3 or n == 0: 
    n = int(input("Recommencez: "))

n = str(n)
c = n[0]
d = n[1]
u = n[2]

print(
    f'Les combinaisons possibles sont: {c+d+u}, {c+u+d}, {d+u+c}, {d+c+u}, {u+d+c}, {u+c+d} \n',
    f'Le produit est: {int(c)*int(d)*int(u)} \n', 
    f'la somme est: {int(c)+int(d)+int(u)}'
)

