# Dado um natural, ele é primo?

n = int(input("Digite um número: "))
primo = True
divisor = 2
metade = n / 2
while divisor <= metade:
    if n % divisor == 0:
        primo = False
    divisor += 1
if n == 2:
    print("É primo")
elif primo:
    print("É primo")
else:
    print("Não é primo")