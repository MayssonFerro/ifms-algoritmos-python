print("Dados três números, qual o maior?")
x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
z = float(input("Digite um número: "))

if x > y:
    maior = x
else:
    maior = y
 
if z > maior:
    maior = z

print("O maior é", maior)