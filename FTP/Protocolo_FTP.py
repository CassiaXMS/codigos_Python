from ftplib import *#Importação de todas as funções do módulo ftplib

ftp_ativo=False #conexão passiva
ftp = FTP('ftp.ibiblio.org') #método FTP com o endereço do ftp
print(ftp.getwelcome()) #método gelwelcome do objeto ftp para retornar uma msg padrão pelo servidor
usuario = input("Digite o usuario:")
senha = input("Digite a senha: ")
ftp.login(usuario, senha)
print("Diretório atual de trabalho: ", ftp.pwd()) #retorna o diretório atual
ftp.cwd("pub")
print("Diretório corrente: ", ftp.pwd()) #deslocar entre os diretórios
print(ftp.retrlines('LIST'))
ftp.quit()