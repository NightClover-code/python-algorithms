#functions
def decimal_to_binary(n):
    t = []
    while (n // 2 != 0):
        r = n % 2 
        t.append(r)
        n //= 2
    t.append(n % 2)
    t.reverse()
    result = ''
    for el in t:
        result += str(el)
    return result

#inputs
n = int(input('Entrez un entier naturel: '))

#guards
while (n < 0):
    n = int(input('Recommencez: '))

#execution
print(decimal_to_binary(n))

