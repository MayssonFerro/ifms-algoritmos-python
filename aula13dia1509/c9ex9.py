# Dado um inteiro, quantos dígitos ele tem? (dica: vai dividindo por 10 até chegar no zero)

num = int(input("Digite um número inteiro: "))
cont = 0

if num < 10:
    cont += 1
    print(f"Esse número tem {cont} digito")
elif 10 <= num > 100:
    print("Esse número tem {cont} digito")