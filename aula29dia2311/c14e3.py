# Receber um número e retornar true caso seja primo, ou false, caso contrário.

def primo(a):
    
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("Digite um número para saber se ele é primo")

    x = int(input("Número: "))

    if primo(x):
        print(f"O número {x} é primo")
    else:
        print(f"O número {x} não é primo")