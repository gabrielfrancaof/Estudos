#Ler vários produtos (código, descrição, quantidade e valor) para uma venda, exibir a lista de produtos e o total da venda.

total_venda = 0
continuar = "s"
lista_produtos = ""

 
while continuar == "s" or continuar == "S":
    codigo_produto = input("Digite o código do produto: ")
    descricao = input("Digite a descrição do produto: ")
    quantidade = int (input ("Digite a quantidade: "))
    valor_produto = float (input ("Digite o valor do produto: R$"))
    sub_total = quantidade*valor_produto
    total_venda += sub_total
    lista_produtos += str(quantidade) + " x " + descricao + "\n"
    continuar = input("Deseja continuar (S/N)?")


print ("-"*30)
print ("Os produtos comprados foram:\n", lista_produtos)
print ("Valor total da compra: R$%.2f" % total_venda)
