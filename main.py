def ler_arquivo():
    with open("notas.csv","r") as arquivo:
        return arquivo.readlines()

def escrever_arquivo(conteudo): 
    with open("notas.csv","a") as arquivo:
        arquivo.write(conteudo+"\n")

conteudo=ler_arquivo()

conteudo_2=[]

for aluno in conteudo:
    aluno_info=aluno.split(";")
    conteudo_2.append(aluno_info)

menu='''
1-Ver notas dos alunos
2-Adicionar um aluno
'''
opcao=input(f"Digite uma opcao: {menu}")

if opcao== "1":
    print(conteudo_2)
if opcao== "2":
    novo_aluno=input("Digite o nome do aluno: ")
    nota_1=input("Digite a nota: ")
    nota_2=input("Digite a nota: ")
    nota_3=input("Digite a nota: ")
    escrever_arquivo(f"{novo_aluno};{nota_1};{nota_2};{nota_3}")
