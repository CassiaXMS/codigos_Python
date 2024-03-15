ips = {}

resp = "S"

while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")

    resp = input("Digigte <S> para continuar: ").upper()
print("\nExibindos os ip´s: ")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])

print("\n\nExibindo máquinas com o mesmo endereço: ")
pesquisa = input(" Digite os dois últimos octetos: ")

print("\nMáquinas no mesmo endereço (redes diferentes) ")
for ip, nome in ips.items():
    if (ip[1] == pesquisa):
        print(nome)

print("\n\nExibindo máquinas na mesma rede: ")
rede = input(" Digite os dois primeiros octetos: ")

for ip, nome in ips.items():
    if (ip[0] == rede):
        print(nome)
