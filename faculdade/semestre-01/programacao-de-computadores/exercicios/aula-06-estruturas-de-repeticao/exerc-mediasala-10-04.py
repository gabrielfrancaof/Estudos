#fazer a soma das médias dos alinos e fazer a somátoria e imprimri a média da sala (5 alunos)

'''
total = 0
media = [5.5, 10.00, 8.00, 1.0, 6.0]
for media in range (6):
    print(media)
    total = total + media

print("A média é: ", total)
'''

#correção

menorMedia = 10.0
maiorMedia = 0
menor = 0
somaMedia = 0
media = [5.5, 10.00, 8.00, 1.0, 6.0]
for media in media:
    somaMedia += media
    print("Media - ", media, "Soma -", somaMedia)
    if (media > maiorMedia):
        maiorMedia = media
    if (media < menorMedia):
        menorMedia = media
    
print (somaMedia)
print ("Media = ", somaMedia / 5)
print ("A maior média é: ", maiorMedia)
print ("A menor média é: ", menorMedia)