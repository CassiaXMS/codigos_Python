#Criando Dicionario

usuarios = { }
print(usuarios)

usuarios = {
    "Well": ["Well Pierre", "24/01/2024", "Recep_01"], # o login é a chave
    "luri": ["Luri Mah", "14/02/2024", "Raiox_03"]
}
print(usuarios)

#Adicionar objetos
usuarios["Nair"] = ["Nair Laira", "24/01/2024", "Raiox_01"]
print(usuarios)

print("------Buscar ------")
print(usuarios.get("Well"))