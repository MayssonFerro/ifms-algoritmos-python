# Dada a data e o número de dias decorridos, qual é a nova data?
data_str = input("Digite a data inicial (formato: AAAA-MM-DD): ")
numero_de_dias = int(input("Digite o número de dias a serem adicionados: "))

ano, mes, dia = map(int, data_str.split('-'))

dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

ano_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
dias_por_mes[2] += ano_bissexto

meses_restantes = numero_de_dias
mes_aux = mes

mes_aux += (meses_restantes - 1) // dias_por_mes[mes_aux]
meses_restantes -= (mes_aux - mes) * dias_por_mes[mes]

ano_aux = ano + (mes_aux - 1) // 12
mes_aux = (mes_aux - 1) % 12 + 1

nova_data_str = f"{ano_aux:04d}-{mes_aux:02d}-{meses_restantes:02d}"
print(f"A nova data após adicionar {numero_de_dias} dias é: {nova_data_str}")
