n = int(input('Quantos amigos você quer adicionar na sua lista? '))

amigos = []
print(f'Ótimo, agora digite o nome de seus {n} amigos:')
for i in range(n):
    amigo = input()
    amigos.append(amigo)
    
print('Ok, agora digite os amigos que você quer remover da sua lista:')
continuar = True
while continuar:
    continuar = False
    ex_amigo = input()
    for i in range(n):
        if amigos[i] == ex_amigo:
            amigos[i] = 0
            continuar = True
            print(f'{ex_amigo} removido da lista!')
            break
print('Sua lista de amigos resultante é:')
print(amigos)