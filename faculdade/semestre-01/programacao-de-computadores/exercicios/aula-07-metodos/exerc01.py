#1- Faça um método que receba como parâmetros o Km inicial, Km final, quantidade de litros gastos e preço do litro. Calcule e mostre: - Distância percorrida; - Consumo médio; - Valor gasto; 
# Faça um programa principal que solicite para o usuário o valor da quilometragem inicial, final, a quantidade de litros gastos e o preço do litro e mostre a distância percorrida, o consumo médio e o valor gasto, para isso utilize o método definido acima.


import metodo01

km_inicial = int(input("Digite o Km inicial: "))
km_final = int(input("Digite o Km final: "))
quantidade_litros = int(input("Digite a quantidade de litros gastos: "))
preco_litro = int(input("Digite o preço por litro: "))
print("-"*30)
metodo01.distancia (km_final, km_inicial,quantidade_litros, preco_litro)
print("-"*30)