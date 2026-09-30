def gerenciar_notas():
    # Garante a criação do arquivo de notas para testes
    with open("notas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;8.5;7.0;9.0\n")
        arquivo.write("Bruno;5.0;6.0;4.5\n")
        arquivo.write("Carlos;7.5;8.0;9.0\n")
        arquivo.write("Daniela;9.0;9.5;10.0\n")
        arquivo.write("Eduardo;4.0;5.0;3.5\n")
        arquivo.write("Fernanda;6.5;7.0;8.0\n")

    lista_alunos = []

    with open("notas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                dados = linha.split(";")
                nome = dados[0]
                n1 = float(dados[1])
                n2 = float(dados[2])
                n3 = float(dados[3])

                aluno = {
                    "nome": nome,
                    "notas": [n1, n2, n3]
                }
                lista_alunos.append(aluno)

    for aluno in lista_alunos:
        media = sum(aluno["notas"]) / len(aluno["notas"])
        status = "Aprovado" if media >= 6.0 else "Reprovado"
        print(f"{aluno['nome']} - Média: {media:.2f} - {status}")

# Chamada da função
gerenciar_notas()