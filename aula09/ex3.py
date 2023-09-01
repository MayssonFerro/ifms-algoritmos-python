print("Alguns desse números é ímpar?")
x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

if x % 2 != 0:
    if y % 2 != 0:
        print("Sim")
    else:
        print("Sim")
elif y % 2 != 0:
    print("Sim")
else:
    print("Não")