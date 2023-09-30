# Dado um número, ele é múltiplo de 3 ou 5, mas não simultaneamente pelos dois?

x = int(input("Digite um número: "))

if x % 3 == 0 or x % 5 == 0:
    print("Não")
elif x % 3 != 0 and x % 5 != 0:
    print("Não")
else:
    print("Sim")