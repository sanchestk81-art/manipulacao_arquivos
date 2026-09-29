from os.path import split


def contar_palavras():
    with open('texto.txt', 'w', encoding="utf-8") as arquivo:
        arquivo.write("Eu gosto muito de assistir formula 1")
        arquivo.write("No meu tempo livre eu gosto de ler diversas coisas")
        arquivo.write("Eu estudo no Senai e eu gosto bastante do meu curso")

    with open('texto.txt', 'r', encoding="utf-8") as arquivo:
        conteudo = arquivo.read().split()
        quantidade_palavras = len(conteudo) #o len conta os caracteres do conteudo que está em lista por causa do split
    print(f"Quantidade de palavras: {quantidade_palavras}")

contar_palavras()