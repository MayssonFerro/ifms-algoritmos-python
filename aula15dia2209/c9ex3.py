# Dados dois números, ambos são pares?

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Sim")
else:
    print("Não")