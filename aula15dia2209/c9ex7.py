# Dados dois números, algum deles NÃO é múltiplo de 5?

x = int(input("Digite um número: "))
y = int(input("Digite um número: "))

if x % 5 != 0 or y % 5 != 0:
    print("Sim")
else:
    print("Não")