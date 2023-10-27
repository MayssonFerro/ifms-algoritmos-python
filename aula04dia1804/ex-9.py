# Joãozinho fez sua viagem até os Estados Unidos. Porém, chegando lá, descobriu que a temperatura é medida em graus Fahrenheit, e não em Celsius. Dada a temperatura em graus Fahrenheit, qual a temperatura correspondente em graus Celsius? 
f = float(input("Digite quantos graus em fahrenheit: "))
c = ((f - 32) * 5) / 9

print("Nos EUA, está fazendo", c, "graus celsius.")