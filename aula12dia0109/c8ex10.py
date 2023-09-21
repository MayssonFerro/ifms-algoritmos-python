# Ler um número inteiro e escrever um valor aleatório com base nesse número: uma letra maiúscula se o usuário inseriu 1, uma letra minúscula se o usuário inseriu 2 e um dígito se o usuário inseriu qualquer valor que não seja 1 ou 2.

import random

n = int(input("Digite um número inteiro: "))

if n == 1 :
    q = 90 - 65 + 1
    s = 65 + int(random.random() * q)
    print(chr(s))
elif n == 2 :
    q = 122 - 97 + 1
    s = 97 + int(random.random() * q)
    print(chr(s))
else:
    print(int(random.random() * 10))