# Dado o preço da etiqueta de um produto e o código da condição de pagamento, qual o valor total a ser pago pelo produto, e, se for o caso, o valor de cada parcela?

preco = float(input("Digite o preço do produto: "))
codigo = int(input("Digite a condição de pagamento: "))

if codigo == 1:
    valor = preco - (0.1 * preco)
    print("O valor total à ser pago será R$", valor)
elif codigo == 2:
    valor = preco - (0.05 * preco)
    print("O valor total à ser pago será R$", valor)
elif codigo == 3:
    valor = preco / 2
    print("O valor total à ser pago será R$", preco, "e cada parcela será", valor)
elif codigo == 4:
    preco = preco + (0.1 * preco)
    valor = preco / 3
    print("O valor total à ser pago será R$", preco, "e cada parcela será", valor)
else:
    print("Código inválido")