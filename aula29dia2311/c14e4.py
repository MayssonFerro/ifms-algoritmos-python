# Receber um número natural, e retornar o próximo primo maior que ele.

import c14e3

def prox_primo(a):
    maior = a
    while c14e3.primo(maior) != True:
        maior += 1
    return maior

print("Digite um número e descubra qual é o próximo primo maior que ele")
x = int(input("Número: "))
print(f"O primo depois de {x} é {prox_primo(x)}")