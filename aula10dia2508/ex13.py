# Dados o peso e a altura de uma pessoa, qual é o seu IMC e a sua condição atual?

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

if imc < 19.1:
        print("Seu IMC é", imc, "e você está abaixo do preso")
elif 19.1 <= imc < 25.8:
        print("Seu IMC é", imc, "e você está no peso ideal")
elif imc >= 25.8:
        print("Seu IMC é", imc, "e você está acima do peso")