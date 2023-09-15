# Dado um caractere, ele é uma letra?

char = input("Digite um caractere: ")
valor = ord(char)

if 65 <= valor <= 90:
    print("Esse caractere é uma letra")
elif 97 <= valor <= 122:
    print("Esse caractere é uma letra")
else:
    print("Esse caractere não é uma letra")