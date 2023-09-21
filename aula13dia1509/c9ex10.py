# Dado um natural, ele é primo?

n = int(input("Digite um número: "))

if n <= 1:
    print(f'{n} não é primo')
elif n == 2:
    print(f'{n} é primo')
elif n % 2 == 0:
    print(f'{n} não é primo')
else:
    div = 3
    div1 = 0
    
    if n == 3:
        print(f'{n} é primo')
    else:
        while div * div <= n:
            if n % div == 0:
                div1 = 1
            div += 2
            
        if div1 == 1:    
            print(f'{n} não é primo')
        else:
            print(f'{n} é primo')