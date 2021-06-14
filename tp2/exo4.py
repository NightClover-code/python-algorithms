#variables
length = 20

#functions
def max_of_nums(t):
    max = t[0]
    for i in range(length):
        if (max < t[i]):
            max = t[i]
    return max, i

#execution
t = [int(input(f"Entrez le nombre à la valeur {i}: ")) for i in range(length)]
max, i = max_of_nums(t)
print(
    f'le maximum des nombres recus est: {max} \n', 
    f'Ce nombre a été saisi à la position: {i}'
)