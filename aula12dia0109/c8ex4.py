# Dados dois inteiros m e n, gerar três inteiros aleatórios entre m e n.

import random

m = int(input("Digite um número inteiro: "))
n = int(input("Digite outro número inteiro: "))
q = n - m + 1

print(m +  int(random.random() * q))
print(m +  int(random.random() * q))
print(m +  int(random.random() * q))