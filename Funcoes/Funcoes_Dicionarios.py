def perguntar():
    return input("\n--- MENU ----\n" +
                 "<I> - Para Inserir um usuário\n" +
                 "<P> - Para Pesquisar um usuário\n" +
                 "<E> - Para Excluir um usuário\n" +
                 "<L> - Para Listar um usuário\n" +
                 "\n O que deseja realizar? ").upper()


def inserir(dicionario):
    dicionario[input("Digite o codigo de lançamento: ").upper()] = [input("\nDigite o login: ").upper(),
                                                                    input("Digite o nome: "),
                                                                    input("Digite a última data de acesso: "),
                                                                    input("Digite a hora (00:00) de acesso: "),
                                                                    input("Digite a última estação acessada: "),
                                                                    input("Digite o nível do usuário: ").upper()]
    salvar(dicionario)
def salvar(dicionario):
    with open("../Dicionarios/bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + " : " + str(valor) + "\n\n")


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print("\nNome...........: " + lista[1])
        print("Último acesso....: " + lista[2])
        print("Última estação...: " + lista[4])


def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
        with open("../Dicionarios/bd.txt", "w") as arquivo:

            for chave, valor in dicionario.items():
                arquivo.write(chave + " : " + str(valor) + "\n")

    print("Objeto excluído!")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("\nObjeto.....")
        print("Login: ", chave)
        print("Dados: ", valor)
