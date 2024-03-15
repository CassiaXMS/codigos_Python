from socket import *

servidor = "localhost"
porta = 43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input("Sua mensagem: "), 'utf-8')
    obj_socket.send(msg)
    resposta = obj_socket.recv(1024)
    print("Respota do Servidor: ", str(resposta)[2:-1])
    if str(msg)[2:-1].upper() == "FIM":
        break
obj_socket.close()
