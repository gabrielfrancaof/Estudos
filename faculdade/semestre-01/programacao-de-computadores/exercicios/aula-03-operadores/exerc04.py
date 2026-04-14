#Escreva um programa em python para calcular o valor de uma prestação em atraso (prestacao). para isso, obtenha o valor da prestação(valorPrestacao), a porcentagem de multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o valor da prestação atualizado, sabendo que: prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

valorPrestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite a porcentagem da multa: "))
qtdeDias = int (input("Digite a quantidade de dias em atraso: "))

prestacao = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

print("O valor da prestação atualizado é R$", prestacao)