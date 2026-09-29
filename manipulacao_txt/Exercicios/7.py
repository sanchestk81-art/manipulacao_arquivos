def encontrar_nome():
    lista_nomes = []
    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            lista_nomes.append(linha.strip())

        pesquisar = input("Digite o nome que você quer pesquisar: ")
        if pesquisar in lista_nomes:
            print("Nome encontrado!")
        else:
            print("Nome não encontrado!")


encontrar_nome()
