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
