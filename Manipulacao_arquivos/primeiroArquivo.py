#Criando o arquivo solucao1

#MODOS
# "w" = abrindo um arquivo de modo de escrita, caso o arquivo exista ele será sobrescrito.
# "r" = abrirá o arquivo somente no modo leitura
# "a" = ler e escrever além de ir adicionando conteúdo no arquivo
# "x" = criar um novo arquivo em modo exclusivo

'''arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Primeiro Arquivo!!")

arquivo.close()'''

#Criando o arquivo solucao2
'''Utilizando o comando WITH o controle de encerramento ficará por conta dele
sem precisar do método close().

quando não é especificado nenhum caminho do arquivo o Python cosiderará
o caminho do código-fonte'''

with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo")

with open("teste.txt", "a") as arquivo:
    arquivo.write("\nContinuação do texto.")