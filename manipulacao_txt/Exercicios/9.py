def mostrar_numeros():
    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("10")
        arquivo.write("11")
        arquivo.write("12")
        arquivo.write("13")
        arquivo.write("14")
        arquivo.write("15")
        arquivo.write("16")
        arquivo.write("17")
        arquivo.write("18")
        arquivo.write("19")
        arquivo.write("20")

    numeros = []
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            # Converte o valor de texto para inteiro (int)
            numero = int(linha)
            # Adiciona na lista
            numeros.append(numero)

    for numero in numeros:
        if numero % 2 == 0:
            print(f"Esses são os numeros pares: {numeros}")

mostrar_numeros()
