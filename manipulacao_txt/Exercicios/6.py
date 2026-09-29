def carregar_nomes():
    nomes = []
    with open('nomes.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            nomes.append(linha.strip()) #Utilize strip() para remover o \n do final de cada linha.
            # O append serve para no Python serve para adicionar um novo elemento ao final de uma lista.
        print(f"lista de alunos: {nomes}")

carregar_nomes()