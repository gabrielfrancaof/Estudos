nome = input("Digite o nome do produto")
vrcompra = float (input("digite o valor"))
vrvenda = 0

if (vrcompra <10):
    vrvenda= vrcompra * 1.7
elif (vrcompra >=10 and vrcompra <30):
    vrvenda= vrcompra * 1.5 
elif (vrcompra >=30 and vrcompra <50 ):
    vrvenda= vrcompra * 1.4
elif (vrcompra >50):
    vrvenda= vrcompra * 1.3
    
print ("Produto...",nome)
print ("Valor venda ", vrvenda)
     