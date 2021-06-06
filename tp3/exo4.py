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