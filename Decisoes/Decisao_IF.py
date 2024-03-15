nome=input("Digite o nome: ")
idade=int(input('Digite a idade: ' ))
doenca_infecctocontagiosa=input('Suspeita de doença infectocontagiosa?').upper()

if idade >= 65:
    print('O paciente ' + nome + ' POSSUI atendimento prioritário!')
elif doenca_infecctocontagiosa=="SIM":
    print('O paciente ' + nome + ' deve ser direcionado para a sala de espera de reserva.')
else:
    print('O paciente ' + nome + ' NÃO possui atendimento prioritário e pode esperar na sala comum!')


#prioridade = 'NÃO'
#if idade >= 65:
#    prioridade = 'SIM'
#print('O paciente ' + nome + ' possui atendimento prioritário? ', prioridade)
#print('FIM')