def find_max(t, n):
    max = t[0]
    for i in range(0, n):
        if (t[i] > max):
            max = t[i]
    return max

def find_min(t, n):
    min = t[0]
    for i in range(0, n):
        if (t[i] < min):
            min = t[i]
    return min

n = int(input("Entrez le nombre d'élements: "))

elements = []

for i in range(0, n):
    ele = int(input(f'Entrez la valeur {i}: '))
    elements.append(ele)
      
print('le max est: ', find_max(elements, n), 'le min est: ', find_min(elements, n))
    
    
