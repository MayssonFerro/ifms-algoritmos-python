# Dada uma letra maiúscula, qual sua correspondente em minúsculo?
letra = input("Digite uma letra: ")

if 65 <= ord(letra) <= 90 :
    min = chr(ord(letra) + 32)
    print(f'A letra minúscula correspondente é {min}')
else:
    print("Isso não é uma letra maiúscula")