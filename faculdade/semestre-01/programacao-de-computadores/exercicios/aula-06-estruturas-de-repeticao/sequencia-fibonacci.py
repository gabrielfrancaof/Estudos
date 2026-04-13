#10 primeiros numeros fibonacci, escolher a quantidade e imprimir

n = int (input("Digite a quantidade da sequencia: ")) 
a = 0
b = 1

print (a, end = " ")
print (b, end = " ")
for fibonacci in range (n): 
    c = a + b 
    print (c, end = " ")
    a = b 
    b = c
