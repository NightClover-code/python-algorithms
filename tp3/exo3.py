#functions
def split_list(t):
    tp = []
    tn = []
    for el in t:
        if el > 0:
            tp.append(el)
        elif el < 0:
            tn.append(el)
        else:
            tp.append(el)
            tn.append(el)
    return f'tp: {tp}', f'tn: {tn}'

#inputs
n = int(input("Entrez le nombre d'élements: "))

#execution
elements = [int(input(f'Entrez la valeur {i}: ')) for i in range(n)]
print(split_list(elements))