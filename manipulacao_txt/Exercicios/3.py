def adicionar_frase():
    frase = input("Digite uma frase: ")
    with open ("frases.txt", "a") as arquivo:
        arquivo.write(frase + "\n")
    print("Frase adicionada com sucesso!")

adicionar_frase()