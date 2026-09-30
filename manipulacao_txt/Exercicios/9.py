def mostrar_numeros():
    # 1. Escrita no arquivo
    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("3\n1\n12\n44\n14\n99\n16\n17\n81\n19\n78\n21\n22\n43\n")

    numeros = []

    # 2. Leitura do arquivo
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            numero = int(linha.strip())
            numeros.append(numero)

    # Lista para guardar apenas os pares
    pares = []

    # 3. Filtrando os números pares
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)  # Adiciona na lista de pares

    # Exibe a lista inteira de uma vez
    print(pares)

mostrar_numeros()