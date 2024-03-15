#solucao 1
acesso=input('Digite o nivel de acesso (ADM, USR ou GUEST): ').upper()
genero=input('Digite o seu genero (FEM/MASC):').upper()

if acesso=="GUEST":
    print('Olá visitante!')
else:
    if acesso=="ADM":
        if genero=="FEM":
            print('Olá administradora!')
        else:
            print('Olá administrador!')

    elif acesso == "USR":
        if genero == "FEM":
            print('Olá usuária!')
        else:
            print('Olá  usuário!')
    else:
        print('Olá desconhecido!')


#solucao 2
nivel=input("Digite o nível de acesso:").upper()
if nivel=="ADM" or nivel=="USR":
    genero=input("Digite o seu gênero:").upper()
    if nivel=="ADM":
        if genero=="FEMININO":
            print('Olá administradora!')
        else:
            print('Olá administrador!')
    else:
        if genero=="FEMININO":
            print('Olá usuária!')
        else:
            print('Olá usuário!')
elif nivel=="GUEST":
    print('Olá visitante!')
else:
    print('Olá desconhecido!')
