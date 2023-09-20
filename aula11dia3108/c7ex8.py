# Dada uma letra e um inteiro N, qual a letra correspondente ao andar N casas à frente da letra lida (ou atrás, se o N for negativo).

letra1 = input("Digite uma letra: ")
n = int(input("Digite um número inteiro: "))

if 65 <= ord(letra1) <= 90 :
    letra2 = chr(ord(letra1) + n)
    print(f'A letra corresponde ao andar {n} casas da letra {letra1} é {letra2}')
elif 97 <= ord(letra1) <= 122 :
    letra2 = chr(ord(letra1) + n)
    print(f'A letra corresponde ao andar {n} casas da letra {letra1} é {letra2}')
else:
    print("Isso não é uma letra")