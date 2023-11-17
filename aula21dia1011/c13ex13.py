n = int(input('Digite a quantidade de itens: '))
lista = []

print(f'Agora digite os {n} itens da lista')
for i in range(n):
    item = input()
    lista.append(item)
    
print(lista)
