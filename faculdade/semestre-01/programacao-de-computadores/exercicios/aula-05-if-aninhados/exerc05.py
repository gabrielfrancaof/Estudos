# ler 4 números inteiros, exibir o maior e o menor deles

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
num4 = int(input("Digite 9 4º número: "))
maior = num1
menor = num1

if num1 > maior:
    maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num4 > maior:
    maior = num4

if num1 < menor:
    menor = num1
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
if num4 < menor:
    menor = num4


print("O maior número é: %d e o menor número é: %d" % (maior, menor))