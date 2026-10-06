import csv

def criar_csv():
    with open("pilotos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["nome","idade","equipe"])

        escritor.writerow(["Oscar","25","Mc laren"])
        escritor.writerow(["Max", "28", "Red Bull"])
        escritor.writerow(["KIMI", "20", "Mercedes"])
#criar_csv()

def salvar_pilotos():
    pilotos = [
        ["Oscar", "25", "Mc laren"],
        ["Max", "28", "Red Bull"],
        ["KIMI", "20", "Mercedes"],
        ["Gabriel", "23", "Audi"],
        ["Rafael", "22", "Haas"],
        ["Carlos", "28", "Williams"],
        ["Charles", "28", "Ferrari"]
    ]

    with open("novo_pilotos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["nome", "idade", "equipe"])
        escritor.writerows(pilotos)

#"salvar_pilotos()

def ler_csv():
    with open("novo_pilotos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        for linha in leitor:
            print(linha[0])

ler_csv()

def exibir_pilotos():
    with open("novo_pilotos.csv", "r", encoding="utf-8") as arquivo:
        pilotos = csv.DictReader(arquivo)

        for piloto in pilotos:
            print(piloto["nome"])

#exibir_pilotos()

def cadastrar_piloto():
    with open("novo_pilotos.csv", "a+",newline="", encoding="utf-8") as arquivo:
        arquivo.seek(0,2)
        nome = input("digite o nome do piloto: ")
        idade = int(input("digite o idade do piloto: "))
        equipe = input("digite o equipe: ")

        escritor = csv.writer(arquivo)
        csv.writer(arquivo)
        escritor.writerow([nome, idade, equipe])

        arquivo.seek(0)
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            print(linha)


#cadastrar_piloto()

def deletar_pilotos():
    with open("novo_pilotos.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        pilotos = list(leitor)

    with open("novo_pilotos.csv", "w", newline="", encoding="utf-8") as arquivo:
        cabecalho = ["nome", "idade", "equipe"]
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)

        escritor.writeheader()

        piloto_apagar = input("digite o nome do piloto que deseja apagar: ")
        for piloto in pilotos:
            if piloto["nome"] != piloto_apagar:
                escritor.writerow(piloto)


#deletar_pilotos()
