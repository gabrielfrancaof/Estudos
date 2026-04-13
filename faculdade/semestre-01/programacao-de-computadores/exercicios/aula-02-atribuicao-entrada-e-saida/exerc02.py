#Escreva um programa em python que solicite ao usuario o salario atual e mostre o salário acrescido de 5% de comissão

salario_atual = float(input("Digite o seu salário atual: "))
comissão = salario_atual + (salario_atual*0.05)

print("O seu salário com a comsissão será: ",comissão)