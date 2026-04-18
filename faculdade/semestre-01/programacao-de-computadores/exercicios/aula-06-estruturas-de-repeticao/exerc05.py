#Temos um grupo de pessoas . Escreva um programa em Python que leia o sexo e a altura de cada pessoa, calcule e mostre a altura média das mulheres e dos homens separadamente . Utilize o comando de repetição que desejar


mulheres = 0
altura_mulheres = 0.00
resp_mulher = "s"

homens = 0
altura_homens = 0.00
resp_homens = "s"


while resp_mulher == "s" or resp_mulher == "S":
    soma_altura_mulheres = (float(input("Digite a altura da mulher: ")))
    altura_mulheres = altura_mulheres + soma_altura_mulheres
    mulheres = mulheres + 1
    resp_mulher = input("Deseja continuar (S/N)? ")

media_mulher = altura_mulheres/mulheres

while resp_homens == "s" or resp_homens == "S":
    soma_altura_homens = (float(input("Digite a altura do homem: ")))
    altura_homens = altura_homens + soma_altura_homens
    homens = homens + 1
    resp_homens = input("Deseja continuar (S/N)? ")

media_homem = altura_homens/homens

print ("A altura média das mulheres são: %.2f, e a altura média dos homens são: %.2f" % (media_mulher, media_homem))
