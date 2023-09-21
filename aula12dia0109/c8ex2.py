# Dado um inteiro n, gerar três inteiros aleatórios entre 0 e n.

import random

n = int(input("Digite um número inteiro: "))

print(int(random.random() * n))
print(int(random.random() * n))
print(int(random.random() * n))