# Dada uma data, qual é o dia da semana correspondente?
D = int(input("Digite uma dia: "))
M = int(input("Digite um mês: "))
Y = int(input("Digite uma ano: "))
J = (1461 * (Y + 4800 + (M - 14) // 12)) // 4 + (367  * (M - 2 - 12 * ((M - 14) // 12))) // 12 - (3 * (( Y + 4900 + (M - 14) // 12) // 100)) // 4 + D - 32075
W = J % 7 + 1

print("O dia da semana é", W)