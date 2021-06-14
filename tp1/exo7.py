import math

def solve_equation(a, b, c):
    x = 0
    if (a != 0):
        delta = b**2 - 4*a*c
        if (delta >= 0):
            if (delta == 0):
                x = -b/2*a
                return x
            else:
                return (-b - math.sqrt(delta) / 2*a, -b + math.sqrt(delta) / 2*a)
        else:
            return 'pas de solution'
    else:
        if (b == 0):
            if (c == 0):
                return 'tout entier est solution'
            else:
                return 'pas de solution'
        else:
            x = -c/b
            return x

a = int(input('Entrez la valeur de a: '))
b = int(input('Entrez la valeur de b: '))
c = int(input('Entrez la valeur de c: '))

print(f'La solution de {a}x² + {b}x + {c} = 0 est: ', solve_equation(a, b, c))