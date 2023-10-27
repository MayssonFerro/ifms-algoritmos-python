print("Dados três inteiros, a soma deles é ímpar?")
x = int(input("Digite um número: "))
y = int(input("Digite um número: "))
z = int(input("Digite um número: "))

if (x + y + z) % 2 != 0:
    print("Sim")
else:
    print("Não")