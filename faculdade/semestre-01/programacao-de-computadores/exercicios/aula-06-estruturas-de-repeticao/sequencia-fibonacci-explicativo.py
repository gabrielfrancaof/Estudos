#sequencia fibonacci

n = int (input("Digite a quantidade da sequencia: ")) #[5]
a = 0
b = 1

print (a, end = " ")
print (b, end = " ")
for fibonacci in range (n): # [0, 1, 2, 3, 4] - quantidade que irá fazer o loop
    c = a + b               # primeiro loop irá colocar c = 0 + 1 (a + b)
    print (c, end = " ")    # print 1
    a = b                   # 0 -> 1 (a, terá o valor adicionado do b (1))
    b = c                   # 1 -> 1 


'''
#segunda sequencia será: 

    c = a + b               # segundo loop irá colocar c = 1 + 1 (novos valores de a, b)
    print (c, end = " ")    # print 2
    a = b                   # 1 -> 1
    b = c                   # 1 -> 2

#terceira sequencia será:
    c = a + b               # terceiro loop irá colocar c = 1 + 2
    print (c, end = " ")    # print 3
    a = b                   # 1 -> 2
    b = c                   # 2 -> 3 




'''