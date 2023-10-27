# Dada uma sequência de duplas de números, representando valores e seus respectivos pesos, seguida por uma dupla de zeros, qual a média ponderada desconsiderando a dupla de zeros?
v = float(input("Digite o valor: "))
p = float(input("Digite o peso: "))

quo = 0
dividendo = 0
divisor = 0

while v > 0 and p > 0:
    quo = v * p
    dividendo += quo
    divisor += p
    media = dividendo / divisor
    v = float(input("Digite o valor: "))
    p = float(input("Digite o peso: "))
print(f'A média ponderada dos valores e dos pesos equivale à {media:.1f}')