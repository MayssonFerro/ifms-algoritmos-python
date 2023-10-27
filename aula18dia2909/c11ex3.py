# Dados dois números inteiros, multiplicá-los usando somas repetidas. Não pode usar o operador de multiplicação "*". Sugestão: usar um laço e o operador de soma (+).

n1 = int(input())
n2 = int(input())
tot = 0

for i in range(0,n1):
    tot += n2
print(tot)