#functions
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

#inputs
n = int(input("Entrez le nombre d'élements: "))

#execution
elements = [int(input(f'Entrez la valeur {i}: ')) for i in range(n)]
      
print(f'le max est: {find_max(elements, n)}', f'le min est: {find_min(elements, n)}')
    
    
