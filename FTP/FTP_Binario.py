from ftplib import *

#Código responsável por baixar um arquivo binário(img)

ftp = FTP('ftp.ibiblio.org') #criar a conexão com o servidor FTP
print(ftp.getwelcome())
ftp.login()

ftp.cwd('/pub/linux/logos/pictures') #Definir o diretório
with open('pai_do_linux', 'wb') as arq:
    ftp.retrbinary('RETR linus-father-of-linux.jpg', arq.write)
ftp.quit()