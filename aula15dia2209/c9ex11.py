# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que a diferença absoluta entre os outros dois. Dados três números, eles formam os lados de um triângulo válido?

n1 = int(input("n1: "))
n2 = int(input("n2: "))
n3 = int(input("n3: "))

if n1 < (n2 + n3) and n1 > ((n2 - n3) or (n3 - n2)):
    print("Esses números formam um triângulo válido.")
elif n2 < (n1 + n3) and n2 > ((n1 - n3) or (n3 - n1)):
    print("Esses números formam um triângulo válido.")
elif n3 < (n1 + n2) and n3 > ((n1 - n2) or (n2 - n1)):
    print("Esses números formam um triângulo válido.")
else:
    print("Esses números são inválidos")