"""exos TP1 initialement séparés dans plusieurs fichiers 
et fusionnés dans celui ci pour l'envoi dans la plateforme moodle"""

#exo1
###########################################
def find_max(t, n):
    max = t[0]
    for i in range(0, n):
        if (t[i] > max):
            max = t[i]
    return max

def find_min(t, n):
    min = t[0]
    for i in range(0, n):
        if (t[i] < min):
            min = t[i]
    return min

n = int(input("Entrez le nombre d'élements: "))

elements = []

for i in range(0, n):
    ele = int(input(f'Entrez la valeur {i}: '))
    elements.append(ele)
      
print('le max est: ', find_max(elements, n), 'le min est: ', find_min(elements, n))
    
    
#exo2
###########################################
def decimal_to_binary(n):
    t = []
    while (n // 2 != 0):
        r = n % 2 
        t.append(r)
        n //= 2
    if (n // 2 == 0):
        t.append(n % 2)
    t.reverse()
    result = ''
    for el in t:
        result += str(el)
    return result

n = int(input('Entrez un entier naturel: '))

while (n < 0):
    n = int(input('Recommencez: '))

print(decimal_to_binary(n))

#exo3
###########################################
def split_list(t):
    tp = []
    tn = []
    for el in t:
        if el > 0:
            tp.append(el)
        elif el < 0:
            tn.append(el)
        else:
            tp.append(el)
            tn.append(el)
    return f'tp: {tp}', f'tn: {tn}'


n = int(input("Entrez le nombre d'élements: "))

elements = []

for i in range(0, n):
    ele = int(input(f'Entrez la valeur {i}: '))
    elements.append(ele)

print(split_list(elements))

#exo4
###########################################
def pypart(n):  
    T = [[0] * (n+1) for p in range(n+1)]
    for n in range(n+1):
        if n == 0:
            T[n][0] = 1
        else:
            for k in range(n+1):
                if k == 0:
                    T[n][0] = 1
                else:
                    T[n][k] = T[n-1][k-1] + T[n-1][k]
    return T

n = int(input('Entrez un entier naturel n: '))

print(f'Triangle de pascal formé de {n}: ')

for i in pypart(n):     
    for j in i:         
        if (j != 0):
            print(j, end="")      
    print("\r")


#exo5
###########################################
def isConsecutive(t, n):
    isTrue = False
    for i in range(0, n - 1):
        if t[i] + 1 == t[i + 1]:
            isTrue = True 
        else:
            isTrue = False
    return isTrue
    

n = int(input("Entrez le nombre d'élements: "))

elements = []

for i in range(0, n):
    ele = int(input(f'Entrez la valeur {i}: '))
    elements.append(ele)

print(isConsecutive(elements, n))

#exo6
###########################################
def transpose(mat, tr, N):
    for i in range(N):
        for j in range(N):
            tr[i][j] = mat[j][i]
  
def isSymmetric(mat, N):
    tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]
    transpose(mat, tr, N)
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != tr[i][j]):
                return False
    return True


n = int(input("Entrez l'ordre de la matrice: "))

matrix= [[input(f"Entrez l'élement [{i}][{j}]") for j in range(n)] for i in range(n)]

if isSymmetric(matrix, n) == True:
    print('symétrique')
else:
    print('non symétrique')

#exo7
###########################################
def isUpperTriangle(matrix, n):
    isTrue = False
    for i in range(1, n):
        for j in range(0, i):
            if (int(matrix[i][j]) != 0):
                isTrue = False
            else:
                isTrue = True
    return isTrue

n = int(input("Entrez l'ordre de la matrice: "))

matrix= [[input(f"Entrez l'élement [{i}][{j}]: ") for j in range(n)] for i in range(n)]


if (isUpperTriangle(matrix, n) == 1):
    print("La matrice est un triangle supérieur")
else:
    print("La matrice n'est pas un triangle supérieur")

#exo8
###########################################
def isLowerTriangle(matrix, n):
    isTrue = False
    for i in range(1, n):
        for j in range(0, i):
            if (int(matrix[i][j]) != 0):
                isTrue = False
            else:
                isTrue = True
    return isTrue

n = int(input("Entrez l'ordre de la matrice: "))

matrix= [[input(f"Entrez l'élement [{i}][{j}]: ") for j in range(n)] for i in range(n)]


if (isLowerTriangle(matrix, n) == 1):
    print("La matrice est un triangle inférieur")
else:
    print("La matrice n'est pas un triangle inférieur")
