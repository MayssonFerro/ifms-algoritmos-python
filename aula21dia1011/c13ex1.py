# Ler uma lista de n itens. Escrever os n itens normalmente em uma linha e do último para o primeiro em outra linha.

n = int(input('qtd de itens: '))
lista = []

for i in range(n):
    numero = input('nome do numero: ')
    lista.append(numero)

print('lista normal')
print(lista)

for i in range(n -1, 0, -1):
    print(lista[i], end = " ")