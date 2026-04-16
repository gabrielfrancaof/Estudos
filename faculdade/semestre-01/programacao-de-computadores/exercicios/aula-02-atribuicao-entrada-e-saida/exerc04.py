#Escreva um programa em python que calcule as duas raizes de uma equação de 2º Grau ax**2+bx+c. conhecendo os valores dos coeficientes da mesma. Suponha que as raizes são reais.


a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

raiz_delta = delta**0.5

x1 = (-b + raiz_delta) / (2*a)
x2 = (-b - raiz_delta) / (2*a)

print ("O valor de de x1 é: ", x1, "e o valor de x2 é: ", x2)
