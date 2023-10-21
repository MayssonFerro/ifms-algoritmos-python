# Dado um inteiro, qual o seu reverso? Exemplo de entrada→saída: 5837→7385.

n = int(input())

while n > 0:
    m = n % 10
    print(m, end="")