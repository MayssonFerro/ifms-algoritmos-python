# Dada uma sequência de inteiros seguida por um múltiplo de 11, 13 ou 17, qual o menor número?

menor = 0

while n % 11 != 0 or n % 13 != 0 or n % 17 != 0:
    n = int(input("Digite um número ou um múltiplo de 11, 13 ou 17 para acabar: "))
    if n <= menor:
        menor = n
        
print("O menor número é ", menor)