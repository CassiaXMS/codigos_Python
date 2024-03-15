#Lista preenchida estaticamente
#lista_estatica = ["xpto", True]
#lista preenchida dinamicamente
#lista_dinamica = [input("Digite o ususario: "), bool(int(input("Está logado? ")))]
#lista vazia
#lista_vaiz = []

#EXERCICIO 1

'''inventario=[]
resposta="S"
while resposta=="S"
   inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número serial: ")))
    inventario.append(input("Departamento: "))
    resposta=input(("Digite /s/ para continuar: ")).upper()

for elemento in inventario:
    print(elemento)
'''


#EXERCICIO 2 - MÚLTIPLAS LISTAS e índices

equipamentos=[]
valores=[]
numeroSerial=[]
departamentos=[]

resposta="S"
while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    numeroSerial.append(int(input("Número serial: ")))
    departamentos.append(input("Departamento: "))
    resposta=input(("Digite /s/ para continuar: ")).upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento: ", (indice+1))
    print("Nome..........: ", equipamentos[indice])
    print("Valor..........: ", valores[indice])
    print("Serial..........: ", numeroSerial[indice])
    print("Departamento..........: ", departamentos[indice])


busca=input("Digite o nome do equipamento: ")
for indice in range(0, len(equipamentos)):
    if busca==equipamentos[indice]:
        print("Valor..........: ", valores[indice])
        print("Serial..........: ", numeroSerial[indice])
