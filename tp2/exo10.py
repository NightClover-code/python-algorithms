#functions
def factorielle(n):
    if (n == 0):
        return 1
    else:
        return n * factorielle(n - 1)

def calcul_suite(n):
    S = 0
    for i in range(n + 1):
        S += 1 / factorielle(i)
    return S

#inputs
n = int(input('Entrez un entier naturel: '))

#execution
print(f'La somme recherchée est: {calcul_suite(n)}')