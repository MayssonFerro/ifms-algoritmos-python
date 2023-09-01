print("Dados dois números, qual o maior deles e a diferença absoluta entre eles?")
x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
if x > y:
    maior = x
    d = x - y
else:
    maior = y
    d = y - x
    
print("O maior número é o", maior, ", e a diferença absoluta entre eles é", d)