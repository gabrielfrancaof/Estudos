#Ler uma quantidade indeterminada de alunos com as seguintes informações RGM, NOME, Sexo e Media. Calcular a media da sala, exibir a media da sala, maior nota, menor nota e a media por sexo.

continuar = "s"
masculino = 0
feminino = 0
media_f = 0
media_m = 0
media_sala = 0
maior_nota = None
menor_nota = None

while continuar == "s" or continuar == "S":
    sexo = input ("Digite o sexo do aluno (M/F):")
    nome = input ("Digite o nome do aluno: ")
    rgm = input ("Digite o RGM do aluno: ")
    media_aluno = float(input("Digite a média do aluno: "))
    media_sala += media_aluno
    if sexo == "m" or sexo == "M":
        masculino += 1
        media_m += media_aluno
    else:
        feminino += 1
        media_f += media_aluno
    if maior_nota is None or media_aluno > maior_nota:
        maior_nota = media_aluno
    if menor_nota is None or media_aluno < menor_nota:
        menor_nota = media_aluno
    continuar = input("Deseja continuar (S/N)?")

if feminino > 0:
    media_f = media_f / feminino
if masculino > 0:
    media_m = media_m / masculino
if (masculino + feminino) > 0:
    media_sala = media_sala / (masculino+feminino)


print("A média da sala é: ", media_sala)
print("A maior nota é: ", maior_nota)
print("A menor nota é: ", menor_nota)
print("A média por sexo masculina é %.2f e a feminina é %.2f" % (media_m, media_f))