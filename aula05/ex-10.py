# Dado o valor do saque realizado pelo cliente de um banco, quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível? Podem ser utilizadas notas de $100, $50, $20, $10, $5, $2 e $1.
valor_saque = int(input("Digite o valor do saque: "))

notas_100 = valor_saque // 100
valor_saque %= 100

notas_50 = valor_saque // 50
valor_saque %= 50

notas_20 = valor_saque // 20
valor_saque %= 20

notas_10 = valor_saque // 10
valor_saque %= 10

notas_5 = valor_saque // 5
valor_saque %= 5

notas_2 = valor_saque // 2
valor_saque %= 2

notas_1 = valor_saque

print(f"{notas_100} notas de $100")
print(f"{notas_50} notas de $50")
print(f"{notas_20} notas de $20")
print(f"{notas_10} notas de $10")
print(f"{notas_5} notas de $5")
print(f"{notas_2} notas de $2")
print(f"{notas_1} notas de $1")
