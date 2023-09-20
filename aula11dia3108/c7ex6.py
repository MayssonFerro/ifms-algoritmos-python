# Dado um caractere, ele é um algarismo?

char = input("Digite um caractere: ")

if 48 <= ord(char) <= 57:
    print("Esse caractere é um algarismo")
else:
    print("Esse caractere não é um algarismo")