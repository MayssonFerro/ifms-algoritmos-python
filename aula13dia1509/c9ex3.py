# Dado um natural n, qual a soma dos pares entre 1 e n?

n = int(input("Digite um número natural: "))
soma = 0
pares = 0

if n > 0:
    while pares <= n:
        soma += pares
        pares += 2
    print(f'O valor da soma dos pares entre 1 e {n}, é {soma}')
else:
    print("Isso não é um número natural")