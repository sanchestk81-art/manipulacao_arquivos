def buscar_produto():
    lista_produtos = []

    # Leitura e montagem da lista de dicionários
    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                nome, preco, quantidade = linha.split(";")
                lista_produtos.append({
                    "nome": nome,
                    "preco": float(preco),
                    "quantidade": int(quantidade)
                })

    termo_busca = input("Digite o produto: ").strip()
    encontrado = False

    for produto in lista_produtos:
        # Compara ignorando letras maiúsculas/minúsculas (.lower())
        if produto["nome"].lower() == termo_busca.lower():
            print("\nProduto encontrado!")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            encontrado = True
            break

    if not encontrado:
        print("\nProduto não encontrado!")

# Chamada da função
buscar_produto()