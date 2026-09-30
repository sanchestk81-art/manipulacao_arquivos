def cadastrar_produtos():
    # Garante a criação do arquivo inicial para testes
    with open("produtos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Teclado;120.50;10\n")
        arquivo.write("Mouse;75.90;15\n")
        arquivo.write("Monitor;899.90;5\n")
        arquivo.write("Headset;150.00;8\n")
        arquivo.write("Webcam;210.00;4\n")

    lista_produtos = []

    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                nome, preco, quantidade = linha.split(";")
                produto = {
                    "nome": nome,
                    "preco": float(preco),
                    "quantidade": int(quantidade)
                }
                lista_produtos.append(produto)

    print(lista_produtos)
    return lista_produtos

# Chamada da função
cadastrar_produtos()