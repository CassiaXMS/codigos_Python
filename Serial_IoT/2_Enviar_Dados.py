import serial

conexao = ""
for porta in range(10): #qual porta o Arduino está  conectado de 0 a 9
    try:
        conexao = serial.Serial("COM" + str(porta), 115200, timeout=0.5)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao != "":
    acao = input("Digite <L> para ligar\n"
                 "<D> para desligar").upper()
    while acao == "L" or acao=="D":
        if acao =="L":
            conexao.write(b'1') #formato byte para transmissão de dados
        else:
            conexao.write('b'0)
        acao = input("Digite <L> para ligar\n"
                    "<D> para desligar").upper()
    conexao.close()
    print("Conexão encerrada!")
    else:
        print("Sem portas disponíveis")
