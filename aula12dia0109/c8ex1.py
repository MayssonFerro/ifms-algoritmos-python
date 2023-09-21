# Dado um inteiro como semente, gerar três inteiros aleatórios.

import random
        
i = int(input("Digite uma semente: "))

random.seed(i)
 
print(random.random())
print(random.random())
print(random.random())