# DECISÕES ENCADEADAS

nome = input("Digite o nome: ")
idade = int(input('Digite a idade: '))
doenca_infecctocontagiosa = input('Suspeita de doença infectocontagiosa?').upper()

if idade >= 65:
    print('Paciente COM prioridade')
    if doenca_infecctocontagiosa == "SIM":
        print('Encaminhe o  patient para sala AMARELA')
    elif doenca_infecctocontagiosa == 'NAO':
        print('Encaminhe o  paciente para sala BRANCA')
    else:
        print('Responda a suspeita com SIM ou NAO')

else:
    print('Paciente SEM prioridade')
    if doenca_infecctocontagiosa == "SIM":
        print('Encaminhe o  paciente para sala AMARELA')
    elif doenca_infecctocontagiosa == 'NAO':
        print('Encaminhe o  paciente para sala BRANCA')
    else:
        print('Responda a suspeita com SIM ou NAO')
