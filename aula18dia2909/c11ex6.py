# Programa de caixa de loja. Ler uma sequência de triplas que correspondem às informações dos produtos comprados: quantidade, preço unitário, nome do produto. Escrever, em uma linha para cada produto, seu nome e o preço total. Escrever na última linha o preço total da compra.

q = int(input("Quantidade: "))

total = 0
tudo = 0

for i in range(1,q+1):
    n = input("Nome: ")
    p = float(input("Preço: "))
    uni = int(input("quantidade: "))
    tudo = p * uni
    total += tudo
    print(f"O total a ser pago pelo produto {n} é de R${tudo}")
print("O total da sua compra é R$", total)