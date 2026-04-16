# Ecreva um programa que solicite ao usuário os valores de três contas de consumo (p.ex. água, luz e telefone) e o valor de seu salário. verifique se o salário é suficiente para pagar as três contas, caso não seja apresente a mensagem "Salário insuficiente". Caso seja, apresente o valor que restou do salário após pagar as contas.

agua = float(input("Digite o valor da sua conta de água: "))
luz = float(input("Digite o valor da sua conta de luz: "))
telefone = float(input("Digite o valor da sua conta de telefone: "))
salario = float(input("Digite o seu salário :"))
soma_contas = agua+luz+telefone
if salario >= soma_contas:
    print ("Você irá conseguir pagar as contas e ainda irá lhe sobrar: R$", salario-soma_contas)
else:
    print("Salário insuficiente")
    print("Para pagar todas as contas, você precisaria de mais: R$", soma_contas-salario)