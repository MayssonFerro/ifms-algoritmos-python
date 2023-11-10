# Dada uma sequência de inteiros, que termina com 10 números ou com um múltiplo de 6. Qual a soma dos múltiplos de 3? O múltiplo de 6 não deve ser contabilizado na soma. Utilize break.

soma = 0
cont = 0

while cont < 10:
    n = int(input("Digite um número: "))
    cont += 1
    
    if n % 6 == 0:
        cont = 10
    
    if n % 3 == 0 and n % 6 != 0:
        soma += n
        
print("A soma dos múltiplos de 3 é", soma)