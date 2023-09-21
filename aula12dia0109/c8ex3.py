# Dado um inteiro n, gerar três inteiros aleatórios entre −n e n.

import random

n = int(input("Digite um número inteiro: "))
q = n - (-n) + 1

print((-n) + int(random.random() * q))
print((-n) + int(random.random() * q))
print((-n) + int(random.random() * q))
