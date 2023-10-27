# Qual a tabuada dos número de 1 a 10?

for num in range(1,11):
    for i in range(1,11):
        atual = num * i
        print(f'{num} * {i} = {atual}')
    print()