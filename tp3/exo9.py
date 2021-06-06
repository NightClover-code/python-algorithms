def decaler_tableau(t, n):
    f = t[0]
    for i in range(n - 1):
        t[i] = t[i + 1]
    t[n - 1] = f
    return t

n = int(input("Entrez l'ordre du tableau : "))

t= [input(f"Entrez l'élement [{i}]: ") for i in range(n)]

print(decaler_tableau(t, n))