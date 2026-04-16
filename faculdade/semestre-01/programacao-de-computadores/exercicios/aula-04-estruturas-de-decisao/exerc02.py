#Crie um algoritimo que solicite ao usuário o seu turno de trabalho e a quantidade de horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a seguir, de acordo com o turno de trabalho. Caso o turno seja igual a 'N' (utilize um caractere para representar) o valor da hora trabalhada é R$45,00, caso o contrário é R$37,50

turno = (input("Digite o seu turno (n ou d): "))
quantidade_horas_trabalhadas = float (input("Digite sua quantidade de horas trabalhadas: "))
valor_do_salario_d = 37.5
valor_do_salario_n = 45

if turno == "n":
    print ("O valor do seu salário é: R$", quantidade_horas_trabalhadas*valor_do_salario_n )
else:
    print("O valor do seu salário é: R$",quantidade_horas_trabalhadas*valor_do_salario_d)