def distancia (km_final, km_inicial,quantidade_litros, preco_litro):
    distancia = km_final - km_inicial
    print("A distancia foi: ", distancia,"km")
    consumo = distancia / quantidade_litros
    print("O consumo foi: ", consumo, "km/l")
    custo = consumo * preco_litro
    print("O valor gasto foi: R$", custo)
    