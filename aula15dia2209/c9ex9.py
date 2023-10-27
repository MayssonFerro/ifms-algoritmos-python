# Dados três números, nenhum deles é múltiplo de 5 e de 3?

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if (n1 % 3 != 0 and n2 % 3 != 0) and (n1 % 5 != 0 and n2 % 5 != 0):
    print("Sim, nenhum é múltiplo de 3 e 5")
else:
    print("Não, pelo menos um deles é mútiplo de 3 e/ou 5")