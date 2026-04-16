# Escreva um algoritimo que solicite um número ao usuário. caso seja digitado um valor entre 0 e 9, mostre: "valor correto", caso contrário mostre: "valor incorreto"

numero = int(input("Digite um número: "))
if numero <=9 and numero >=0:
    print ("Valor correto")
else:
    print("Valor incorreto")