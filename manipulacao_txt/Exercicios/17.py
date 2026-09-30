def calcular_estoque():
    lista_produtos = []

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

    # Variável acumuladora
    valor_total = 0.0

    for produto in lista_produtos:
        subtotal = produto["preco"] * produto["quantidade"]
        valor_total += subtotal  # Acumula o subtotal de cada produto

    print(f"Valor total do estoque: R$ {valor_total:.2f}")

# Chamada da função
calcular_estoque()