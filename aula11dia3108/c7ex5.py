# Dada uma letra, ela é vogal ou consoante?

letra = input("Digite uma letra: ")

if 97 <= ord(letra) <= 122:
    if ord(letra) == 97:
        print(f"A letra '{letra}' é uma vogal.")
    elif ord(letra) == 101:
        print(f"A letra '{letra}' é uma vogal.")
    elif ord(letra) == 105:
        print(f"A letra '{letra}' é uma vogal.")
    elif ord(letra) == 111:
        print(f"A letra '{letra}' é uma vogal.")
    elif ord(letra) == 117:
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")
else:
    print("Por favor, insira uma única letra minúscula válida.")





