#Boletim do 1 A
def calcular_media (a, b):
    return(a + b)/2
escola = "EEMTIFC"
total = int(input("QTD ALUNOS"))
medias = []
nomes = []
aprovados = 0
recuperacao = 0
reprovados = 0
I = 1
while I <= total:
    print("aluno", I, ".")
    nome = input("nome: ")
    n1 = float(input("nota1: "))
    n2 = float(input("nota2: "))
    media = calcular_media(n1, n2)
    nomes.append(nome)
    medias.append(media)
    nota_baixa = n1 < 4 or n2 < 4
    passou = media >= 6 and not nota_baixa
    if passou:
        print(nome, "- Aprovado")
        aprovados += 1
    elif media >= 4:
        print(nome, "- Recuperacao")
        recuperacao += 1
    else:
        print(nome, "- Reprovado")
        reprovados += 1
    I = I + 1
soma = 0
for m in medias:
    soma = soma + m
print("escola: ", escola)
print("Media da turma: ", aprovados, "de", total)
print("Aprovados: ", aprovados, "de", total)
print("De Recuperacao: ", recuperacao, "de", total)
print("Reprovado: ", reprovados, "de", total)

boletim = list(zip(nomes, medias))
boletim.sort()
for nome, media in boletim:
     print(nome, ":", media, "Media Final")