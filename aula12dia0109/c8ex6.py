# Gerar dois inteiros aleatórios cuja soma esteja entre [0 e 100).

import random

n1 = int(random.random() * 100)
n2 = int(random.random() * 100 - n1)
soma = n1 + n2

print(n1)
print(n2)
print(soma)