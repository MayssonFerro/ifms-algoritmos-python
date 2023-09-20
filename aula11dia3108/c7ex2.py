# Dado um caractere, ele é uma letra?

char = input("Digite um caractere: ")

if 65 <= ord(char) <= 90:
    print("Esse caractere é uma letra")
elif 97 <= ord(char) <= 122:
    print("Esse caractere é uma letra")
else:
    print("Esse caractere não é uma letra")