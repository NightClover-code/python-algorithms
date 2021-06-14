#functions
def isUpperTriangle(matrix, n):
    for i in range(1, n):
        for j in range(0, i):
            if (int(matrix[i][j]) != 0):
                return False
    return True

#inputs
n = int(input("Entrez l'ordre de la matrice: "))

#execution
matrix= [[input(f"Entrez l'élement [{i}][{j}]: ") for j in range(n)] for i in range(n)]

if (isUpperTriangle(matrix, n)):
    print("La matrice est un triangle supérieur")
else:
    print("La matrice n'est pas un triangle supérieur")
