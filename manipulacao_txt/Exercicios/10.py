def separar_numeros():
    numeros = []
    pares=[]  # Lista para guardar apenas os pares
    impares=[]
    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            numero = int(linha.strip())
            numeros.append(numero)

        # 3. Filtrando os números pares
        for numero in numeros:
            if numero % 2 == 0:
                pares.append(numero)  # Adiciona na lista de pares
            # 4. Filtrando os numeros Impares
        for numero in numeros:
            if numero % 1 == 0:
                impares.append(numero)

            # Exibe a lista inteira de uma vez
    print(f"numeros pares: {pares}")
    print(f'numeros impares: {impares}')

separar_numeros()