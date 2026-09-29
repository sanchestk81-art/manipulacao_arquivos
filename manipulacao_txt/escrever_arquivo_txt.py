# Modo "r" - Abre o arquivo para a leitura
# Modo "w" - Abre para escrita e apaga o conteúdo existente
# Modo "a" - Adiciona novo conteúdo no final do arquivo
# Modo "x" - Cria um arquivo novo e gera erro se ele já existir

def criar_arquivo():
    # O "with" fecha o arquivo automaticamente
    # O "open()" função para leitura ou escrita de arquivos
    with open('aluno.txt', 'w', encoding="utf-8") as arquivo: # o "as arquivo" estamosdando um apelido para a função
        arquivo.write("Nome: sanches\n")
        arquivo.write("famoso escolhido: OSCAR PIASTRI 81\n")
        arquivo.write("Cor: laranja\n")
        #arquivo.close() precimos colocar esse close quando não utilizarmos o with no começo do codigo

#criar_arquivo()

def adicionar_aluno(nome):
    with open('aluno.txt', 'a', encoding="utf-8") as arquivo: #o enconding serve para entender os acentos em porutugues
        arquivo.write(nome + "\n")

#adicionar_aluno("Flávia")
#adicionar_aluno("Isadora")
#adicionar_aluno("Angelina")
#adicionar_aluno("Maria Eduarda")

def listar_alunos():
    with open('aluno.txt', 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print(f"O conteudo do arquvo alunos é {conteudo}")

#listar_alunos()

def listar_alunos_individual():
    lista_alunos = []
    with open('aluno.txt', 'r', encoding="utf-8") as arquivo:
       for linha in arquivo:
           lista_alunos.append(linha.strip())
    print(f"lista de alunos: {lista_alunos}")

    #nome_alunos = [nome.strip() for nome in arquivo]

#listar_alunos_individual()

def cadastrar_alunos():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    with open("cadastro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write( f"{nome} | {idade}\n")

    print ("Aluno cadastrado com sucesso!")
#cadastrar_alunos()

def listar_cadastro():
    itens_cadastro = []
    with open('cadastro.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(";")
            obj ={
                "nome": nome,
                "idade": idade
            }

            itens_cadastro.append(obj)

    print(f"Itens cadastrados: {itens_cadastro}")

listar_cadastro()


