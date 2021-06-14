#inputs
n = int(input('Entrez un entier: '))
print(f'Triangle assossié à {n}: ')

#logic
for i in range(1, n + 1):
    print('\r')
    for j in range(1, i + 1):
        print(j, end="")
