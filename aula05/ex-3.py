# Dados dois números inteiros m e n, qual é o primeiro múltiplo de m maior que n? Por exemplo, para m=17 e n=50, o primeiro múltiplo de 17 após 50 é 51.
m = int(input("Digite um número: "))
n = int(input("Digite outro número: "))

primeiro_multiplo = (n // m + 1) * m

print("O primeiro múltiplo de", m ,"maior que", n, "é:", primeiro_multiplo)
