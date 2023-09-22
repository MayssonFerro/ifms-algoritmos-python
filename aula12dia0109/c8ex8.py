# Gerar uma senha aleatória de 8 dígitos com letras maiúsculas, minúsculas e inteiros.
import random

cont = 1
while cont <= 8:
    c1 = int(random.random()*62)
    if c1 < 26:
        c1 += 97
        c1 = chr(c1)
    elif c1 < 52:
        c1 += 39
        c1 = chr(c1)
    else:
        c1 -= 4
        c1 = chr(c1)
    print(c1, end=" ")
    cont += 1