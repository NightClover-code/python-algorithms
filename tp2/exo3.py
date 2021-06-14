#functions
def somme_chiffres(n):
    S = 0
    t = []
    for char in n:
        t.append(char)
    for item in t:
        S += int(item)
    return S

#execution
n = input('Entrez un entier naturel: ')
print(f'La somme des chiffres de {n} est: {somme_chiffres(n)}')