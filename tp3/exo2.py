def decimal_to_binary(n):
    t = []
    while (n // 2 != 0):
        r = n % 2 
        t.append(r)
        n //= 2
    if (n // 2 == 0):
        t.append(n % 2)
    t.reverse()
    result = ''
    for el in t:
        result += str(el)
    return result

n = int(input('Entrez un entier naturel: '))

while (n < 0):
    n = int(input('Recommencez: '))

print(decimal_to_binary(n))

