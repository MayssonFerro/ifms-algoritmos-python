# Dado o código de determinado produto, qual a sua classificação?

codigo = int(input("Digite o código do produto: "))

if codigo == 1:
    print("Alimento não perecível")
elif codigo >= 2:
    if codigo <= 4:
        print("Alimento perecível")
    elif codigo >=5:
        if codigo <= 6:
            print("Vestuário")
        elif codigo == 7:
            print("Higiene pessoal")
        elif codigo >= 8:
            if codigo <= 15:
                print("Limpeza e utensílios domésticos")
            else: print("Inválido")