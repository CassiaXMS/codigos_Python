
#EXERCICIO DE DEPRECIAÇÃO DO VALOR DO PRODUTO
equipamentos=[]
valores=[]
seriais=[]
departamentos=[]

resposta="S"
while resposta=="S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número serial: ")))
    departamentos.append(input("Departamento: "))
    resposta=input(("Digite /s/ para continuar: ")).upper()

depreciacao=input("Digite o nome do equipamento a ser depreciado: ")
for indice in range(0, len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo..........: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Valor atual..........: ", valores[indice])



#EXERCICIO DE EXCLUSÃO

excluirSerial=int(input("Digite o serial do produto a ser excluído: "))
for indice in range(0, len(equipamentos)):
    if excluirSerial == seriais[indice]:
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        del departamentos[indice]
        break

for indice in range(0, len(equipamentos)):
    print("Equipamento: ", (indice+1))
    print("Nome..........: ", equipamentos[indice])
    print("Valor..........: ", valores[indice])
    print("Serial..........: ", seriais[indice])
    print("Departamento..........: ", departamentos[indice])

