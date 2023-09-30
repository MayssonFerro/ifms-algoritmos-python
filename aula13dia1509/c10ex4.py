# Dada a quantidade de estudantes da turma de Algoritmos, seguida pelas notas das provas de cada estudante, qual a maior nota e a média das notas dessa turma?

q = int(input("Digite a quantidade de estudantes: "))
contador = 0
media = 0
maior = 0

while contador < q:
    n = float(input("Digite a nota de cada estudante: "))
    
    if 0 <= n <= 10:
        media += n
        contador += 1
        
        if n >= maior:
            maior = n
    else:
        print("Nota invalida, tente novamente")    
        
media /= q

print(f"A maior nota da sala foi {maior}, e a média da sala é {media}")