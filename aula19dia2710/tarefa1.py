# Dada uma sequência de 10 inteiros, qual a soma dos múltiplos de 3? Entretanto, múltiplos de 6 não devem ser contabilizados na soma. Utilize continue.

soma = 0

for i in range(10):
    n = int(input("Digite um número: "))
    if n % 3 == 0 and n % 6 != 0:
        soma += n
        
print("A soma dos múltiplos de 3 é", soma)