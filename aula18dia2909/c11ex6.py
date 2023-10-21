# Programa de caixa de loja. Ler uma sequência de triplas que correspondem às informações dos produtos comprados: quantidade, preço unitário, nome do produto. Escrever, em uma linha para cada produto, seu nome e o preço total. Escrever na última linha o preço total da compra.

q = int(input("Quantidade: "))
p = float(input("Preço: "))
n = input("Nome: ")
total = 0

if q != 0:
    total = q * p