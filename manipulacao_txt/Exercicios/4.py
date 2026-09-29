
def contar_linhas():
    with open("nomes.txt", "w", encoding ="utf-8") as arquivo:
        arquivo.write("Oscar\n")
        arquivo.write("Carlos\n")
        arquivo.write("Max\n")
        arquivo.write("Verstappen\n")
        arquivo.write("Piastri\n")
        arquivo.write("Sainz\n")

    with open ("nomes.txt", "r", encoding="utf-8") as arquivo:
        quantidade_linhas = sum(1 for linha in arquivo) #Lê a quantidade de linhas no arquivo
    print(f"A quantidade de linhas no aqurivo é de {quantidade_linhas}")

contar_linhas()

#No pimeiro with mudei a letra de 'a' para 'w' pois a cada vez em que eu fui testar o programa
# A quantidade de linhas aumentava



