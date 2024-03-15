from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

endereco=input("Digite um endereco com número e cidade. "
               "Exemplo: avenida paulista, 100 São Paulo:")
resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0]!='None':
    print("Endereço completo.: ", resultado)
    print("Bairro............: ", resultado[1])
    print("Cidade............: ", resultado[2])
    print("Regiao............: ", resultado[3])