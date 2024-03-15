import serial


#conexao = serial.Serial('COM3', 115200, timeout=0.5) #objeto conexao responsavel pela saída serial utilizado no Arduino
# O segundo parâmetro do método serial() indica o "Baud Rate" é a capacidade
# de transmissão de bits por segundo, existem alguns valores que são padrão, exemplo 9600

conexao = ""
for porta in range(10): #qual porta o Arduino está  conectado de 0 a 9
    try:
        conexao = serial.Serial("COM" + str(porta), 115200, timeout=0.5)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao != "":
    conexao.close()
    print("Conexão encerrada!")
else:
    print("Sem portas disponíveis")

