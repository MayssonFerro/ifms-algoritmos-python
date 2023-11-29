# Receber dois números e retornar sua soma.

def soma(a, b):
    s = a + b
    return s

print("Digite dois números para saber a soma deles")
x = int(input("X= "))
y = int(input("Y= "))
z = soma(x, y)

print(f"A soma dos números {x} e {y} é {z}")