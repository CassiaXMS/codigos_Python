import getpass

usuario = getpass.getuser()
senha = getpass.getpass("Digite a senha... ")

if usuario == "Pars" and senha == "joj8":
    print("Usuário logado")
else:
    print("Login Negado")
