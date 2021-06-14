#variables
i = 100

#logic
while (100 <= int(i) <= 999):
    i = str(i)
    c = i[0]
    d = i[1]
    u = i[2]
    if (int(i) == int(c)**3 + int(d)**3 + int(u)**3):
        print(i)
    i = int(i) + 1
