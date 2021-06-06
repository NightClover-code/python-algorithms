a = int(input('Entrez un nombre a: '))
b = int(input('Entrez un nombre b: '))
op = input('Entrez un opérateur. Choix possibles: +, *, /, - \n')

printMsg = 'le résultat est: '

if (op == '+'):
    print(printMsg, a + b)
elif (op == '*'):
    print(printMsg, a * b)
elif (op == '/'):
    print(printMsg, a / b)
elif (op == '-'):
    print(printMsg, a - b)
else: 
    print('Opérateur erroné')