# O Máximo Divisor Comum (MDC) é o maior número que divide dois ou mais números simultaneamente, e corresponde ao produto dos divisores comuns entre dois ou mais números inteiros. A decomposição simultâneas é um método para encontrar o MDC de dois ou mais números e consiste em dividir varias vezes os números dados pelo menor fator primo, e se o número não for divisível pelo menor fator, ele deve ser repetido. O MDC é obtido pela multiplicação dos fatores primos comuns, ou seja, os fatores que dividem os números dados simultaneamente.
# Receber dois naturais e retornar seu MDC.

def mdc(a, b):
    mdc_atual = 1
    for divisor in range(2, a + 1):
        if a % divisor == 0 and b % divisor == 0:
                mdc_atual = divisor
    return mdc_atual


if __name__ == "__main__":
    print("Digite dois números naturais: ")
    x = int(input("X: "))
    y = int(input("Y: "))

    d = mdc(x, y)

    print(f"O mdc de {x} e {y} é {d}")