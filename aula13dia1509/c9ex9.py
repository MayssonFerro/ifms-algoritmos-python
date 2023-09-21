# Dado um inteiro, quantos dígitos ele tem? (dica: vai dividindo por 10 até chegar no zero)

n = int(input("Digite um número inteiro: "))
cont = 0

while n > 0:
    n //= 10
    cont += 1
print(f'Esse número tem {cont} dígitos')    
