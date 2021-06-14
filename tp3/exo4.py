#functions
def pypart(n):  
    T = [[0] * (n+1) for i in range(n+1)]
    for n in range(n+1):
        if n == 0:
            T[n][0] = 1
        else:
            for j in range(n+1):
                if j == 0:
                    T[n][0] = 1
                else:
                    T[n][j] = T[n-1][j-1] + T[n-1][j]
    return T

#inputs
n = int(input('Entrez un entier naturel n: '))

#executions
print(f'Triangle de pascal formé de {n}: ')

for i in pypart(n):     
    for j in i:         
        if (j != 0):
            print(j, end="")      
    print('\r')
