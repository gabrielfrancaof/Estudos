#Elabore um programa em Python que implemente uma calculadora com as funções de somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) e a seguir calcular e mostrar o resultado.

numero1 = float (input("Digite o primeiro número: "))
operacao = (input("Digite a operação (+, -, *, / ): "))
numero2 = float (input("Digite o segundo número: "))


if operacao == "+":
    soma = numero1 + numero2
    print ("O resultado da soma é:", soma)
elif operacao == "-":
    subtrair = numero1 - numero2
    print ("O resultado da subtração é:", subtrair)
elif operacao == "*":
    multiplicacao = numero1 * numero2
    print ("O resultado da multiplicação é:", multiplicacao)
elif operacao == "/":
    if numero1 == 0 or numero2 == 0:
        print("Não é possível dividir por zero!")
    else:
        dividir = numero1 / numero2
        print ("O resultado da divisão é:", dividir)
else:
    print("Operação inválida. Tente novamente usando +, -, * ou /.")