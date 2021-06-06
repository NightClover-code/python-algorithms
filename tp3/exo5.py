def isConsecutive(t, n):
    isTrue = False
    for i in range(0, n - 1):
        if t[i] + 1 == t[i + 1]:
            isTrue = True 
        else:
            isTrue = False
    return isTrue
    

n = int(input("Entrez le nombre d'élements: "))

elements = []

for i in range(0, n):
    ele = int(input(f'Entrez la valeur {i}: '))
    elements.append(ele)

print(isConsecutive(elements, n))