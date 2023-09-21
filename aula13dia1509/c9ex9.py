# Dado um inteiro, quantos dígitos ele tem? (dica: vai dividindo por 10 até chegar no zero)

n = int(input("Digite um número inteiro: "))
cont = 0
div = n

if n >= 0:
    while div > 0:
        div //= 10
        cont += 1
    print(f'Esse número tem {cont} dígitos')    
else:
    print("Digite um valor inteiro")
    