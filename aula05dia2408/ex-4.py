# Dado um número inteiro representando um tempo em segundos, qual é o tempo em horas, minutos e segundos?
x = int(input("Digite o tempo em segundos: "))
s = x % 60
y = x // 60
m = y % 60
h = y // 60

print("A data é: ", h,":", m, ":", s)  