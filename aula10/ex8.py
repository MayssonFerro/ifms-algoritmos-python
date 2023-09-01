print("Dados três números representando os lados de um triângulo, ele é equilátero, isósceles ou escaleno?")
x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
z = float(input("Digite um número: "))

if x == y == z:
        print("O triângulo é equilátero")
elif x == y != z:
        print("O triangulo é isósceles")
else:
    x != y != z