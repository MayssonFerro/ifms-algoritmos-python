# Dadas duas letras, quantas letras há entre as duas?

letra1 = input("Digite uma letra: ")
letra2 = input("Digite outra letra: ")

if 65 <= ord(letra1) <= 90 :
    if 65 <= ord(letra2) <= 90 :
        if ord(letra1) < ord(letra2) :
            n = ord(letra2) - ord(letra1) - 1
            print(f'Há {n} letra(s) entre {letra1} e {letra2}')
        else:
            n = ord(letra1) - ord(letra2) - 1
            print(f'Há {n} letra(s) entre {letra1} e {letra2}')
            
elif 97 <= ord(letra1) <= 122 :
    if 97 <= ord(letra2) <= 122 :
        if ord(letra1) < ord(letra2) :
            n = ord(letra2) - ord(letra1) - 1
            print(f'Há {n} letra(s) entre {letra1} e {letra2}')
        else:
            n = ord(letra1) - ord(letra2) - 1
            print(f'Há {n} letra(s) entre {letra1} e {letra2}')

else:
    print("Pelo menos um desses caracteres não é uma letra")