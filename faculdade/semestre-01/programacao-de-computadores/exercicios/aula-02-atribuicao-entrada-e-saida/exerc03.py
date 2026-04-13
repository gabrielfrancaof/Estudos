#Escreva um programa em python que solicite ao usuario a distância entre duas cidades e o tempo de viagem. O programa deverá calcular e exibir a velociade média de um carro que vai de uma cidade para outra usando a formula VM = distancia / tempo

distancia = int(input("Digite a distância entre as duas cidades: "))
tempo = int(input("Digite o a duração da viagem: "))
velocidade = distancia / tempo

print("A velocidade média do carro é de: ", velocidade,"km/h")