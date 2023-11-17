# Dado um inteiro, qual o seu reverso? Exemplo de entrada→saída: 5837→7385.

orig = int(input())
resto = 0
inv = 0

while orig != 0:
    resto = orig % 10
    inv = inv * 10 + resto
    orig = orig // 10
print(inv)