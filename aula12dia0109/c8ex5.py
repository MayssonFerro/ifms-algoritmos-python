# Dados dois inteiros m e n, gerar três inteiros aleatórios múltiplos de m entre 0 e n.

import random

m = int(input("Digite um número inteiro: "))
n = int(input("Digite outro número inteiro: "))
q = n // m + 1

print(m * int(random.random() * q))
print(m * int(random.random() * q))
print(m * int(random.random() * q))