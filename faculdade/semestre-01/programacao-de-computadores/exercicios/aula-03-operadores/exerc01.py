#Faça um programa em python que calcule e mostre o valor do volume do tronco de uma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura do tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e calcular a seguinte expressão: volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 *Bmenor**2)**0.5)

altura = float(input("Digite a altura do tronco: "))
base_maior = float(input("Digite o valor da base maior: "))
base_menor = float(input("Digite o valor da base menor: "))
expressao = (altura / 3) *(base_maior**2 + base_menor**2 + (base_maior**2 *base_menor**2)**0.5)

print("O volume do tronco da pirâmide é: ", expressao)