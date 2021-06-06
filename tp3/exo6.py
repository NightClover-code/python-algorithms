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