import csv

def pokemons():
    # 1. Criando a lista de dados inicial
    treinadores = [
        ["Ash Ketchum", "Kanto", "90"],
        ["Misty", "Kanto", "75"],
        ["Brock", "Kanto", "78"],
        ["May", "Hoenn", "70"],
        ["Dawn", "Sinnoh", "68"],
        ["Iris", "Unova", "80"],
        ["Cilan", "Unova", "72"],
        ["Serena", "Kalos", "66"],
        ["Kiawe", "Alola", "74"],
        ["Goh", "Kanto", "65"]
    ]

    # 2. Salvando os dados no arquivo treinadores.csv
    with open("treinadores.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["nome", "regiao", "nivel"])  # Cabeçalho
        escritor.writerows(treinadores)                 # Escreve as linhas

    # 3. O Loop do Menu
    while True:
        print("\n===== TREINADORES POKÉMON =====")
        print("1 - Listar todos os treinadores")
        print("2 - Buscar treinador pelo nome")
        print("3 - Listar treinadores de uma região")
        print("4 - Mostrar treinador com maior nível")
        print("5 - Mostrar treinador com menor nível")
        print("6 - Sair")

        resposta = input("\nDigite sua opção: ")

        # -------------------------------------------------------------
        # OPÇÃO 1: Listar todos
        # -------------------------------------------------------------
        if resposta == "1":
            with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)
                print("\n--- LISTA DE TREINADORES ---")
                for linha in leitor:
                    # Imprime o nome, a região e o nível da pessoa
                    print(f"Nome: {linha['nome']} | Região: {linha['regiao']} | Nível: {linha['nivel']}")

        # -------------------------------------------------------------
        # OPÇÃO 2: Buscar pelo nome
        # -------------------------------------------------------------
        elif resposta == "2":
            nome_digitado = input("Digite o nome do treinador: ")
            encontrado = False

            with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:
                    # Verifica se o nome digitado é igual ao nome no arquivo
                    if nome_digitado.lower() == linha["nome"].lower():
                        print(f"\nEncontrado: {linha['nome']} - Região: {linha['regiao']} - Nível: {linha['nivel']}")
                        encontrado = True

            if encontrado == False:
                print("Treinador não encontrado!")

        # -------------------------------------------------------------
        # OPÇÃO 3: Buscar por região
        # -------------------------------------------------------------
        elif resposta == "3":
            regiao_digitada = input("Digite a região (ex: Kanto, Unova, Alola): ")
            encontrado = False

            with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)
                print(f"\n--- Treinadores de {regiao_digitada} ---")
                for linha in leitor:
                    if regiao_digitada.lower() == linha["regiao"].lower():
                        print(f"Nome: {linha['nome']} | Nível: {linha['nivel']}")
                        encontrado = True

            if encontrado == False:
                print("Nenhum treinador encontrado nessa região!")

        # -------------------------------------------------------------
        # OPÇÃO 4: Mostrar o maior nível
        # -------------------------------------------------------------
        elif resposta == "4":
            maior_nivel = 0
            nome_do_maior = ""

            with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:
                    nivel_atual = int(linha["nivel"])  # Converte o nível de texto para número
                    if nivel_atual > maior_nivel:
                        maior_nivel = nivel_atual
                        nome_do_maior = linha["nome"]

            print(f"\nTreinador com maior nível: {nome_do_maior} (Nível {maior_nivel})")

        # -------------------------------------------------------------
        # OPÇÃO 5: Mostrar o menor nível
        # -------------------------------------------------------------
        elif resposta == "5":
            menor_nivel = 9999  # Começamos com um número bem alto para poder comparar
            nome_do_menor = ""

            with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
                leitor = csv.DictReader(arquivo)
                for linha in leitor:
                    nivel_atual = int(linha["nivel"])
                    if nivel_atual < menor_nivel:
                        menor_nivel = nivel_atual
                        nome_do_menor = linha["nome"]

            print(f"\nTreinador com menor nível: {nome_do_menor} (Nível {menor_nivel})")

        # -------------------------------------------------------------
        # OPÇÃO 6: Sair
        # -------------------------------------------------------------
        elif resposta == "6":
            print("Saindo do programa... Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Executando a função
pokemons()