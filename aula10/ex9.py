# Dado o consumo de uma residência em kWh, qual o preço da energia a ser pago?
faixa = int(input("Digite a faixa em kWh: "))

if faixa <= 500:
    valor = faixa * 0.40
else: valor = faixa * 0.50

print("O preço da energia a ser pago é de R$", valor)