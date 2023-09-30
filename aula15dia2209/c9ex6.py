# Dados três números, todos são múltiplos de 10?

x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
z = int(input("Digite um número: "))

if x % 10 == 0 and y % 10 == 0 and z % 10 == 0:
    print("Sim")
else:
    print("Não")