def ler_arquivo():
    with open("notas.csv","r") as arquivo:
        return arquivo.readlines()

def escrever_arquivo(alunos): 
    with open("notas.csv","a") as arquivo:
        arquivo.write(alunos + "\n")
        
def verificar_nota(nota):
    if nota=="" or nota=="\n":
        return "Nota nao cadastrada!"
    else:
        return nota

def exibir_arquivo(alunos):
    for aluno in alunos:
        print(f"\nNome: {aluno[0]}")
        print(f"Nota 1: {verificar_nota(aluno[1])}")
        print(f"Nota 2: {verificar_nota(aluno[2])}")
        print(f"Nota 3: {verificar_nota(aluno[3])}")
        print(f"Nota 4: {verificar_nota(aluno[4])}")
        
def alterar_nota():

conteudo=ler_arquivo()
lista_alunos=[]

for aluno in conteudo:
    aluno_info=aluno.split(";")
    lista_alunos.append(aluno_info)

menu='''
1-Ver notas dos alunos
2-Adicionar um aluno
3-Adicionar nota de um aluno
'''
opcao=input(f"Digite uma opcao: {menu}")

if opcao== "1":
    exibir_arquivo(lista_alunos)
if opcao== "2":
    novo_aluno=input("Digite o nome do aluno: ")
    escrever_arquivo(f"{novo_aluno};;;;")
if opcao== "3":
    nome_aluno=input("Digite o nome do aluno: ")
    nota_1=input("Digite a nota: ")
    #nota_2=input("Digite a nota: ")
    #nota_3=input("Digite a nota: ")
    #nota_4=input("Digite a nota: ")