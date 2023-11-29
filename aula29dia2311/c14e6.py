# Podemos calcular o MMC de dois naturais através do seu MDC, pela fórmula: mmc(a,b)= a*b/mdc(a,b). Receber dois naturais e retornar seu MMC, usando a função mmc do exercício anterior como base.

import c14e5

def mmc(a, b):
    m = (a * b) // c14e5.mdc(a, b)
    return m


print("Digite dois números para achar seu MMC")
x = int(input("X: "))
y = int(input("Y: "))

z = mmc(x, y)

print(f"O MMC desses números é {z}")