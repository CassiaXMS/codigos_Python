#ListasDentroDelistas

inventario=[]

resposta="S"
while resposta=="S":
    equipamento=[input("\n Equipamento: "),
                float(input(" Valor: ")),
                int(input(" Número serial: ")),
                input(" Departamento: ")]
    inventario.append(equipamento)
    resposta=input("\n  Digite \"s\" para continuar: ").upper()

for elemento in inventario:
    print("\n Nome........:", elemento[0])
    print(" Valor........:", elemento[1])
    print(" Número Serial........:", elemento[2])
    print(" Departamento........:", elemento[3])
    print()\

busca=input("\nDigite o NOME do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca==elemento[0]:
        print(" Valor........:", elemento[1])
        print(" Número Serial........:", elemento[2])
        print() \

depreciacao=input("\nDigite o nome do equipamento que será depreciado: ")
for elemento in inventario:
    if depreciacao==elemento[0]:
        print("Valor antigo........:", elemento[1])
        elemento[1]=elemento[1]*0.9
        print("Valor novo........:", elemento[1])
        print()\

serial=int(input("Digite o SERIAL do equipamento a ser excluído: "))
for elemento in inventario:
    if serial == elemento[2]:
        inventario.remove(elemento)


for elemento in inventario:
    print("\n Nome........:", elemento[0])
    print(" Valor........:", elemento[1])
    print(" Número Serial........:", elemento[2])
    print(" Departamento........:", elemento[3])


# FUNÇÕES PARA LISTAS NÚMERICAS

valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("\nO equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de:", sum(valores))
