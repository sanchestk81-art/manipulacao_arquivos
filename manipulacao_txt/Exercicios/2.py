def criar_arquivo():
    frase = input("digite sua frase:")
    with open ("frase.txt", "a", encoding= "utf-8") as arquivo:
        arquivo.write(f"{frase}\n")
    print("O conteudo foi colocado com sucesso!")

    with open ("frase.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print(f"O conteudo do arquivo é: {conteudo}")
criar_arquivo()

#Na atividade não estava falando para mostrar
# mas eu fiz uma linha para mostrar o que foi digitado