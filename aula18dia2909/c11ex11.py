# Dado um natural no sistema decimal, qual seu equivalente no sistema binário? Para realizar a conversão do sistema decimal para binário, realiza-se a divisão sucessiva por 2. O resultado da conversão será dado pelo último quociente (MSB) e o agrupamento dos restos das divisões.

# 5387 em binario eh 1010100001011
 
n = int(input())
resto = 0
b = 0
inv = 0

while n != 0:
    resto = n % 2
    b = b * 10 + resto
    n = n // 2
    
while b != 0:
    resto = b % 10
    inv = inv * 10 + resto
    b = b // 10
print(b)

corrigir = 1   