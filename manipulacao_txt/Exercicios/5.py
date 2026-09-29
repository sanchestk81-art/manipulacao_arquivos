def contar_caracter():
    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        quantidade = len(conteudo)
        print(f"Quantidade de caracteres: {quantidade}")
contar_caracter()