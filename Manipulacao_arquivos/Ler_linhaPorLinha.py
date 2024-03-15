#Leitura do arquivo linha por linha

with open("arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)