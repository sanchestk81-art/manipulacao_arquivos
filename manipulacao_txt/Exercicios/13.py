def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Ler arquivo")
        print("2. Escrever no arquivo")
        print("3. Sobescrever no arquivo")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("no arquivo tem escrito:")
            with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
                lerarquivo = arquivo.read()
                print(lerarquivo)

        elif opcao == "2":
            print(">> Executando a opção 2...")
            escreva = input("escreva no arquivo: ")
            with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
              arquivo.write(escreva)

        elif opcao == "3":
            print(">> Executando a opção 3")
            sobescreva = input("escreva sobre as informações do arquivo: ")
            with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(sobescreva)

        elif opcao == "4":
            print("Saindo do programa... Até mais!")
            break  # Encerra o laço 'while' e sai do menu

        else:
            print("Opção inválida! Tente novamente.")


# Chamada da função
menu()