#for numero in range(1, int(input("Digite um número para determinar o fim: ")), 1):
 #   print("  " + str(numero))

#   EXPLICAÇÃO
# Para o laço FOR criamos um variável denominada numero
# em segui umafunção, o range() em que determina um faixa de valores a ser incrementada
# range(1) significa que variável iniciará com valor 1 em seguida até o valor que o usuário digitar,
#por último ela será incrementada de 1 em 1


# EXERCICIO DA TABUADA
numero=int(input("Digite o numero: "))
print("Tabuada do numero:  " , numero)

for valor in range(1,11,1):
    print(str(numero) + " x " + str(valor) + " = " + str(numero*valor))