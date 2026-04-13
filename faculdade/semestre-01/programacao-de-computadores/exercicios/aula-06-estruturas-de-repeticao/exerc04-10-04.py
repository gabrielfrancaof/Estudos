num1 = float (input("Numero1: "))
num2 = float (input("Numero2: "))
operacao = input ("Operação: ")
res = 0
erro = 0
if (operacao == '+'):
    res = num1 + num2
elif (operacao == '-'):
    res = num1 - num2
elif (operacao == '*'):
    res = num1 * num2
elif (operacao == '/'):
    if (num2 == 0):
        print ("Erro: não é possivel dividir por 0 !")
    else:
        res = num1 / num2
else:
    print ("Operação invalida")
    erro == 1
if (erro == 0):    
    print ("Resultado = ", res)