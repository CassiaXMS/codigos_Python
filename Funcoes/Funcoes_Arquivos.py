def chamarMenu():
    escolha = int(input("\n--- MENU ----\n" +
                        "<1> - Para registrar ativo\n" +
                        "<2> - Para persistir em arquivo\n" +
                        "<3> - Para exibir arquivos armazenados: \n" +
                        " O que deseja realizar? ").upper())
    return escolha


def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número do patrimonial: ")] = [
            input("\nDigite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
        resp = input("\nDigite <S> para continuar: ").upper()


def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
    return "Persistido com sucesso!"


def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas
