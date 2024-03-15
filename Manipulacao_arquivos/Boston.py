# Exercício manipulando arquivos de terceiros
#Arquivo baixado "Economic-indicators" - https://data.boston.gov/dataset/economic-indicators-legacy-portal.

with open("economic-indicators.csv", "r") as boston:
    totalVoos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0

    ano_usuario = input("Digite o ano que deseja pesquisar? ")
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        totalVoos = totalVoos + float(lista[1])

        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        if ano_usuario == lista[0]:
            total_passageiros = total_passageiros + float(lista[2])
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]

    print(" O total de voos são: ", totalVoos)
    print(" O (mês/ano) de maior movimento no aeroporto foi: ", str(mes), "/", str(ano))
    print(" O total de passageiros do ano ", ano_usuario, " foi de ", total_passageiros)
    print(" O mês do ano ", ano_usuario, " com maior media para diária de hotel foi ", mes_maior_diaria)



