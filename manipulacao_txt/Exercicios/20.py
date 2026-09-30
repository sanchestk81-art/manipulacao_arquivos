def carregar_dados():
    alunos = []
    try:
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    id_aluno, nome, idade, curso = linha.split(";")
                    alunos.append({
                        "id": int(id_aluno),
                        "nome": nome,
                        "idade": int(idade),
                        "curso": curso
                    })
    except FileNotFoundError:
        # Se o arquivo não existir, cria o arquivo com o conteúdo inicial
        conteudo_inicial = [
            "1;Ana Silva;17;Desenvolvimento de Sistemas\n",
            "2;Bruno Souza;18;Desenvolvimento de Sistemas\n",
            "3;Carlos Oliveira;17;Desenvolvimento de Sistemas\n",
            "4;Daniela Santos;18;Desenvolvimento de Sistemas\n",
            "5;Eduardo Lima;17;Desenvolvimento de Sistemas\n"
        ]
        with open("alunos.txt", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(conteudo_inicial)
        return carregar_dados()  # Recarrega após criar

    return alunos


def salvar_dados(alunos):
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            linha = f"{aluno['id']};{aluno['nome']};{aluno['idade']};{aluno['curso']}\n"
            arquivo.write(linha)


def sistema_alunos():
    alunos = carregar_dados()

    while True:
        print("\n===== SISTEMA DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            print("\n--- Lista de Alunos ---")
            for a in alunos:
                print(f"{a['id']} - {a['nome']} - {a['idade']} anos")

        elif opcao == "2":
            id_busca = int(input("Digite o ID: "))
            encontrado = False
            for a in alunos:
                if a["id"] == id_busca:
                    print(f"\nAluno encontrado:\n{a['nome']}\n{a['idade']} anos\n{a['curso']}")
                    encontrado = True
                    break
            if not encontrado:
                print("\nAluno não encontrado!")

        elif opcao == "3":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")

            # Gera um ID automático maior que o maior ID existente
            novo_id = max([a["id"] for a in alunos], default=0) + 1

            novo_aluno = {"id": novo_id, "nome": nome, "idade": idade, "curso": curso}
            alunos.append(novo_aluno)
            salvar_dados(alunos)
            print("\nAluno cadastrado com sucesso!")

        elif opcao == "4":
            id_remover = int(input("Digite o ID do aluno a remover: "))
            tamanho_anterior = len(alunos)
            alunos = [a for a in alunos if a["id"] != id_remover]

            if len(alunos) < tamanho_anterior:
                salvar_dados(alunos)
                print("\nAluno removido com sucesso!")
            else:
                print("\nAluno não encontrado!")

        elif opcao == "5":
            id_alterar = int(input("Digite o ID do aluno a alterar: "))
            encontrado = False
            for a in alunos:
                if a["id"] == id_alterar:
                    a["nome"] = input(f"Novo nome ({a['nome']}): ") or a["nome"]
                    idade_in = input(f"Nova idade ({a['idade']}): ")
                    a["idade"] = int(idade_in) if idade_in else a["idade"]
                    a["curso"] = input(f"Novo curso ({a['curso']}): ") or a["curso"]

                    salvar_dados(alunos)
                    print("\nDados alterados com sucesso!")
                    encontrado = True
                    break
            if not encontrado:
                print("\nAluno não encontrado!")

        elif opcao == "6":
            print("\nSaindo do sistema...")
            break

        else:
            print("\nOpção inválida!")


# Chamada do sistema
sistema_alunos()