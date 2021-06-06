def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

n = int(input("Entrez l'ordre du tableau : "))

t= [input(f"Entrez l'élement [{i}]: ") for i in range(n)]

print('normal: ', t)

reverseList(t, 0, n - 1)

print('reversed: ', t)
