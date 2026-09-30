def gerar_relatorio():
    # Criando arquivo inicial de vendas
    with open("vendas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;Notebook;3500.00\nBruno;Mouse;80.00\nCarlos;Teclado;150.00\n")
        arquivo.write("Ana;Monitor;900.00\nDaniela;Notebook;3500.00\nBruno;Headset;200.00\n")
        arquivo.write("Carlos;Mouse;80.00\nAna;Teclado;150.00\nDaniela;Monitor;900.00\n")

    vendas = []

    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                vendedor, produto, valor = linha.split(";")
                vendas.append({
                    "vendedor": vendedor,
                    "produto": produto,
                    "valor": float(valor)
                })

    total_vendas = 0.0
    contagem_vendas = {}
    totais_por_vendedor = {}

    for venda in vendas:
        total_vendas += venda["valor"]
        vendedor = venda["vendedor"]

        # Contagem da quantidade de vendas
        contagem_vendas[vendedor] = contagem_vendas.get(vendedor, 0) + 1

        # Soma do total acumulado de cada vendedor (para o desafio)
        totais_por_vendedor[vendedor] = totais_por_vendedor.get(vendedor, 0.0) + venda["valor"]

    print(f"TOTAL DE VENDAS: R$ {total_vendas:.2f}\n")
    print("Quantidade de vendas:")
    for vendedor, qtd in contagem_vendas.items():
        print(f"{vendedor}: {qtd}")

    # Desafio Adicional: Maior vendedor em valor
    top_vendedor = max(totais_por_vendedor, key=totais_por_vendedor.get)
    print(f"\nTop vendedor em valor: {top_vendedor} (R$ {totais_por_vendedor[top_vendedor]:.2f})")


# Chamada da função
gerar_relatorio()