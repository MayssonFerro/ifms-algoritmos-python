# Dada uma sequência de números seguida pelo número zero, qual a soma dos números?

soma = 0
num = int(input())

while num != 0:
    print("+", num, end=" ")
    soma += num
    int(input())
print("=", soma) 

