# Dada uma sequência de números que termina quando sua soma ultrapassar 1000, qual o maior número?

soma = 0
maior = 0

while soma <= 1000:
    n = int(input("Digite um número: "))
    
    soma += n
    
    if n >= maior:
        
        maior = n
    
print(f'O maior número da sequência é {maior}')