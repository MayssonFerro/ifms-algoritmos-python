# Receber três números, representando, respectivamente, dia, mês e ano, e retornar a data por extenso. Por exemplo, para os argumentos (7, 12, 2022), retornar a string "7 de dezembro de 2022".

def ext(a):
    meses = ["zero","janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    nome = meses[a]
    return nome

print("Digite uma data")
d = int(input("Dia: "))
m = int(input("Mês: "))
ano = int(input("Ano: "))

print(f"Dia {d} de {ext(m)} de {ano}")