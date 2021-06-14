#functions
def isConsecutive(t, n):
    isTrue = False
    for i in range(n - 1):
        if t[i] + 1 == t[i + 1]:
            isTrue = True 
        else:
            isTrue = False
    return isTrue
    
#inputs
n = int(input("Entrez le nombre d'élements: "))

#execution
elements = [int(input(f'Entrez la valeur {i}: ')) for i in range(n)]

print(isConsecutive(elements, n))