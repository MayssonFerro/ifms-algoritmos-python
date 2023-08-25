# Dada uma data, qual é o seu dia juliano?

D = int(input("Digite uma dia: "))
M = int(input("Digite um mês: "))
Y = int(input("Digite uma ano: "))

a = (14 - M) // 12
y = Y + 4800 - a
m = M + 12 * a - 3
J = D + ( 153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045

print("O dia juliano dessa data é:", J) 