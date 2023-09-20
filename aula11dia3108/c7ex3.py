# Dada uma letra, qual a sua posição no alfabeto, sendo ‘a’ a posição 1 e ‘z’ a posição 26?

letra = input("Digite uma letra: ")

if 97 <= ord(letra) <= 122:
    posicao = ord(letra) - 97 + 1
    print(f"A letra '{letra}' está na posição {posicao} no alfabeto.")
elif 65 <= ord(letra) <= 90 :
    posicao = ord(letra) - 65 + 1
    print(f"A letra '{letra}' está na posição {posicao} no alfabeto.")
else:
    print("Isso não é uma letra, colega")