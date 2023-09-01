print("Dados dois inteiros, ambos são pares?")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

if x % 2 == 0:
    if y % 2 == 0:
        print("Sim")
    else:
        print("Não")