# Dada uma sequência de números seguida pelo número zero, qual a soma dos números?

n = int(input("Digite um número, ou 0 para sair: "))
soma = 0

while n != 0:
    soma += n
    n = int(input("Digite um número, ou 0 para sair: "))
    
print(f'A soma desses números é {soma}')