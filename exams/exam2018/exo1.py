def saisie(n):
    t = [ ([0] * n) for i in range(n)]
    for i in range(n):
        for j in range(n):
            print('t [', i, '][', j, ']=', end="")
            t[i][j] = int(input())
    return t

def maxFunc(t):
    o = []
    for i in t:
        for j in i:
            o.append(j)
    return max(o)

def diagonaleSom(t):
    S = 0
    n = len(t)
    for i in range(n):
        for j in range(n):
            if i == j:
                S += t[i][j]
    return S

matriceLen = int(input('Entrez la longueur de la matrice: '))
print(diagonaleSom(saisie(matriceLen)))

