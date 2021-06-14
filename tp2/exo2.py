#functions
def calcul_pgcd(a, b):
    while(a % b != 0):
        r = a % b
        a = b
        b = r
    if (a % b == 0):
        return b

#inputs
a = int(input('Entrez a positif et non nul: '))
b = int(input('Entrez b positif et non nul: '))

#guards
while(a < 0 or b < 0):
    a = int(input('Recommencez, entrez a: '))
    a = int(input('Recommencez, entrez b: '))

#execution
print(f"le pgcd de {a} et {b} est: {calcul_pgcd(a, b)}")
