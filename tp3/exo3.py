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


n = int(input("Entrez le nombre d'élements: "))

elements = []

for i in range(0, n):
    ele = int(input(f'Entrez la valeur {i}: '))
    elements.append(ele)

print(split_list(elements))