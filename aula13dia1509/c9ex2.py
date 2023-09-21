# Qual o intervalo de inteiros de cada item a seguir?

i1 = 1
c1 = 0
while 0 < i1 < 10:
    i1 += 1
    c1 += 1
print(f'a. Existem {c1} intervalos entre [0,10[')

i2 = 9
c2 = 0
while 10 > i2 > 0:
    i2 -= 1
    c2 += 1
print(f'b. Existem {c2} intervalos entre ]10,0]')

i3 = -10
c3 = 0
while -10 <= i3 <= 10:
    i3 += 1
    c3 += 1
print(f'c. Existem {c3} intervalos entre [-10,10]')

i4 = 100
c4 = 0
while 100 >= i4 >= 1:
    i4 -= 1
    c4 += 1
print(f'd. Existem {c4} intervalos entre [100,1]')