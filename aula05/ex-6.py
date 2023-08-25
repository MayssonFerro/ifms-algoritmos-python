# Dado um dia juliano, qual é a data correspondente?
J = int(input("Digite um dia juliano: "))
f = J+1401+(4*J+274277)//146097*3//4+(-38)
e = 4*f+3
g = e%1461//4
h = 5*g+2
D = h%153//5+1
M = (h//153+2)%12+1
Y = e//1461-4716+(12+2-M)//12

print("A data correspondente é: ", D, ":", M,":", Y)


