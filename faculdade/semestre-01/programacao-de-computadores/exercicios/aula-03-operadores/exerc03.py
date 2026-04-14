#Crie um programa que solicite ao usurário a sua idade expressa em anos, meses e dias (variaveis separadas). Calcule e mostre a idade expressa apenas em dias. para isso considere 1 ano = 365 dias, 1 mês = 30 dias.

anos = int(input("Digite quantos anos você tem: "))
meses = int(input("Digite quantos meses a mais você tem: "))
dias = int(input("Digite seus dias a mais: "))

formula = (anos*365) + (meses*30) + dias

print("A sua idade expressa é ",formula,"dias!")

