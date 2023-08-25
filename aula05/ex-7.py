# Dado um dia juliano, qual é o dia da semana?
J = int(input("Digite um dia juliano: "))
W = J % 7 + 1

print("O dia da semana é", W)