# Gerar uma letra aleatória entre 'a' e 'z'

import random

quantidade = 122 - 97 + 1
sorteado = 97 + int(random.random() * quantidade)

print(chr(sorteado))