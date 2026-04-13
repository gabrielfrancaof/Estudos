#Escreva um programa em python que leia a cotação do dólar (taxa de conversão), leia um valor em dolares e converta e mostre o valor equivalente em reais

cotacao_dolar = float(input("Digite a cotação atual do dólar: "))
valor_em_dolar = float(input("Digite o valor que deseja converter: "))
taxa_conversao = valor_em_dolar * cotacao_dolar

print ("O valor de $", valor_em_dolar, "dólares em reais é de: R$", taxa_conversao )