#Identificando as funções


#Adicionar item ao inventário
def preencherInventario(lista):
    resposta="S"
    while resposta == "S":
        equipamento=[input("\n Equipamento: "),
                    float(input(" Valor: ")),
                    int(input(" Número serial: ")),
                    input(" Departamento: ")]
        lista.append(equipamento)
        resposta=input("\n  Digite \"s\" para continuar: ").upper()

#Exibir dados do inventário
def exibirInventario(lista):
    for elemento in lista:
        print("\n Nome........:", elemento[0])
        print(" Valor........:", elemento[1])
        print(" Número Serial........:", elemento[2])
        print(" Departamento........:", elemento[3])
        print()\

#Localizar um item no inventário por nome
def localizarPorNome(lista):
    busca=input("\nDigite o NOME do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca==elemento[0]:
            print(" Valor........:", elemento[1])
            print(" Número Serial........:", elemento[2])
            print() \

# Depreciar item no inventário
def depreciarPorNome(lista, porc):
    depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao==elemento[0]:
            print("Valor antigo........:", elemento[1])
            elemento[1]=elemento[1]*(1-porc/100)
            print("Valor novo........:", elemento[1])
            print()\

# Excluir item do inventário
def excluirPorSerial(lista):
    serial=int(input("Digite o SERIAL do equipamento a ser excluído: "))
    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
    return "Itens excluídos"


# FUNÇÕES PARA LISTAS NÚMERICAS
#Resumo dos valores do inventário
def resumirValores(lista):
    valores=[]
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores)>0:
        print("\nO equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de:", sum(valores))
