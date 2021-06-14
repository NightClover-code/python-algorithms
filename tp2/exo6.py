#functions
def calculate_sum(n):
    S = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            S += i + j
    return S
        
#inputs
n = int(input('Entrez un entier naturel n >= 1: '))

#guards
while(n < 1):
    n = int(input('Recommencez: '))

#execution
print(f"La somme recherchée est: {calculate_sum(n)}")