n = input("Entrez un nombre de 3 chiffres: ")

while len(n) != 3 or int(c) == 0 or int(d) == 0 or int(u) == 0: 
    c = n[0]
    d = n[1]
    u = n[2]
    n = input("Recommencez: ")

c = n[0]
d = n[1]
u = n[2]

print(
    f'Les combinaisons possibles sont: {c+d+u}, {c+u+d}, {d+u+c}, {d+c+u}, {u+d+c}, {u+c+d} \n',
    f'Le produit est: {int(c)*int(d)*int(u)} \n', 
    f'la somme est: {int(c)+int(d)+int(u)}'
)
