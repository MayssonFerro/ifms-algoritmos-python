# Dado um número inteiro representando um ano qualquer, este ano é bissexto?

ano = int(input())

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print("É bissexto")
else:
    print("Não é bissexto")