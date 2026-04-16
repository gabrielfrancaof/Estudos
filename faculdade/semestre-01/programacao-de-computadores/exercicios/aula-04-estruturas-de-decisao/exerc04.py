#Faça um programa que obtenha o valor de uma compra, calcular e mostrar o valor da compra considerando o desconto, conforme descrito: para compras acima de R$200 a loja dá um descontro de 20%, para as avaixo disso não tem descontro, mostre o valor da compra

valor_compra = float(input("Digite o valor da compra: R$ "))
if valor_compra > 200:
    print ("O valor da compra é: R$",valor_compra - (valor_compra*0.2))
else:
    print ("O valor da compra é: R$", valor_compra)