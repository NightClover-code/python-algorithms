#variables
length = 9

#logic
for i in range(length + 1):
    for j in range(length + 1):
        for k in range(length + 1):
            if (i + j + k == 15):
                print(i, j, k)

