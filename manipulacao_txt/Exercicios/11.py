def listar_aprovados():
    # 1. Criação do arquivo (corrigido para \n)
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;8.5\nBruno;5.0\nCarlos;7.2\nDaniela;9.0\nEduardo;4.5\nFernanda;6.8\nGabriel;5.9\n")

    aprovados = []

    # 2. Leitura e processamento do arquivo
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()  # Remove espaços e a quebra de linha extra
            if linha:              # Garante que a linha não esteja vazia
                # Separa o nome e a nota
                nome, nota_str = linha.split(";")
                nota = float(nota_str)  # Converte a nota de texto para decimal (float)

                # Regra: Nota maior ou igual a 6.0
                if nota >= 6.0:
                    aprovados.append(f"{nome} - {nota}")

    # 3. Exibição dos alunos aprovados
    print("Alunos aprovados:")
    for aluno in aprovados:
        print(aluno)

# Chamada da função
listar_aprovados()