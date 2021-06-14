#functions
def isLowerTriangle(matrix, n):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (int(matrix[i][j]) != 0):
                return False
    return True

#inputs
n = int(input("Entrez l'ordre de la matrice: "))

#execution
matrix= [[input(f"Entrez l'élement [{i}][{j}]: ") for j in range(n)] for i in range(n)]

if (isLowerTriangle(matrix, n)):
    print("La matrice est un triangle inférieur")
else:
    print("La matrice n'est pas un triangle inférieur")
