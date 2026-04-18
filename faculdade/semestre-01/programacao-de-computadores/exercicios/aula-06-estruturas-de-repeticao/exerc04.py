#Escreva um algoritmo que leia um grupo de valores reais e determine quantos valores são positivos e quantos são negativos. Determine, também, qual é o menor desses valores. Utilize o comando de repetição que desejar.

positivos = 0
negativos = 0
menor = None
continuar = "s"

while continuar == "s" or continuar == "S":
    grupo = float(input("Digite um valor real: "))
    if grupo >= 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
    if menor is None or grupo < menor:
        menor = grupo
    continuar = input("Deseja continuar (S/N?)")

print("Você digitou %d valores positivos, %d negativos e o menor valor é o %.2f" %(positivos, negativos, menor))
