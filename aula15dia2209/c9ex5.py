# Dados dois números, um deles é múltiplo do outro?

x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

if x % y == 0 or y % x == 0:
    print("Sim")
else:
    print("Não")