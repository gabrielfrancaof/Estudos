#Faça um programa que peça do usuário um valor em graus para um ângulo. Converta-o para raidanos e, usando funções da bliblioteca math, imprima o seno, cosseno e tangente deste ângulo

import math

graus = int(input("Digite o valor em graus: "))

radiano = math.radians(graus)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print("O valor do seno é: ", seno,", O valor do cosseno é: ",cosseno,", e o valor da tangente é: ", tangente)