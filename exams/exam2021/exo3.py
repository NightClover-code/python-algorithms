def factorielle(n):
    if (n == 0):
        return 1
    else:
        return n * factorielle(n - 1)


def puissance(x, n):
    S = 1
    for i in range(0, n):
        S *= x
    return S


def calculateSum(x, n):
    S = 0
    for i in range(0, n):
        N = 2*i + 1
        S += puissance(x, N) / factorielle(N)
    return S




x = float(input("Entrez x: "))
n = int(input("Entrez n: "))

print("Voila Sinhx: ", calculateSum(x, n))



