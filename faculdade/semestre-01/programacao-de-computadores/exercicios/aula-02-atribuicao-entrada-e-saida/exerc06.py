#Escreva um programa em python que leia um valor representando o gasto realizado por um cliente do restaurante ComaBem e visualize o valor total a ser pago, considerando os 10% do garçom

valor_gasto = float(input("Digite o valor gasto no restaurante ComaBem: "))
comissao = valor_gasto *0.1
total = valor_gasto + comissao

print ("O valor de consumo foi: R$", valor_gasto)
print ("A taxa do garçon (10%) foi: R$", comissao)
print ("O valor total da conta é: R$", total)