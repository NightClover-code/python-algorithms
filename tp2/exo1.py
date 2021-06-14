#functions
def somme_impairs(n):
    i = 1
    S = 0
    while (i < n):
        S += i
        i += 2     
    return S   

#inputs
n = int(input('Entrez un entier naturel: '))

#execution
print(f'La somme des impairs inférieurs à {n} est: {somme_impairs(n)}')