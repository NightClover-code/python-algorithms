#functions
def fibonacci(n):
    if (n < 2):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#inputs
n = int(input('Entrez un entier naturel positif: '))

#guards
while (n < 0):
    n = int(input('Recommencez: '))

#execution
print(f'Le {n}eme terme de la suite de fibonnaci est: {fibonacci(n)}')