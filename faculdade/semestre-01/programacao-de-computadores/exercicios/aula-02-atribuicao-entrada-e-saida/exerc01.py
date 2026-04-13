#Desenvolva um programa em python que solicite ao usario os valores dos lados de um retângulo e calcule e mostre seu perímetro e sua área

lado1 = int(input("Digite o valor do primeiro lado: "))
lado2 = int(input("Digite o valor do segundo lado: "))
perimetro = (lado1*2)+(lado2*2)
area = lado1*lado2

print ("O perimetro do rentângulo é: ", perimetro, ",sendo a sua área: ", area)