from socket import *

servidor="localhost" # localhost
porta = 43210  # porta de entrada

obj_socket = socket(AF_INET, SOCK_STREAM)  # identificar os pacotes
obj_socket.bind((servidor,  porta))  # transporte do pacote protocolo TCP
obj_socket.listen(3)  # máximo 2 clientes no servidor
print("Aguardando cliente .....")

while True:
    con, cliente = obj_socket.accept()
    print("Conectando com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos ", msg_recebida)[2:-1]
        msg_enviada = bytes(input("Sua resposta: "), 'utf-8')  # mensagem em formato bytes
        con.send(msg_enviada)
        break
    con.close()
