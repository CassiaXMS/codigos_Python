from Funcoes_modulos.FuncoesComListas import *

minhaLista=[]
print("--Preenchendo")
preencherInventario(minhaLista)
print("\n--Exibindo")
exibirInventario(minhaLista)

print("\n--Pesquisando")
localizarPorNome(minhaLista)
print("\n--Alterando")
depreciarPorNome(minhaLista, 20)

print("\n--Excluindo")
excluirPorSerial(minhaLista)
exibirInventario(minhaLista)

print("\n--Resumindo")
resumirValores(minhaLista)