# Dada uma letra, ela é maiúscula ou minúscula?

letra = input("Digite uma letra: ")
codigo = ord(letra)

if 65 <= codigo <= 90:
    print("letra maiúscula")
elif 97 <= codigo <= 122:
    print("letra minúscula")
else:
    print("isso não é letra parça")