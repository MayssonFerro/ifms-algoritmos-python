# Dados três números, todos são múltiplos de 5 ou de 3?

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if (n1 % 3 == 0 and n2 % 3 == 0) or (n1 % 5 == 0 and n2 % 5 == 0):
    print("Sim")
else:
    print("Não")