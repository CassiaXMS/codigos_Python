<h1 align="center">
    <a>🔗 Introduction to Python 🐍</a>
	
</h1>

> [!NOTE]
>  Parte destas anotações é baseada no [curso online de Python da Faculdade FIAP](https://on.fiap.com.br/)

**Resumo:** Python é uma linguagem livre, multiparadigma, híbrida (compilada e interpretada), alto nível.
Linguagem simples para aprender e muito utilizada no mundo de segurança da informação.

---

## 🏷️ Conteúdo

- [Variáveis](#variáveis)
- [Tomadas de decisão](#tomadas-de-decisão)
- [Laços de repetições](#laços-de-repetições)
- [Listas](#listas)
- [Funções](#funções)
- [Dicionários](#dicionários)
- [Tuplas](#tuplas)
- [Manipulação de arquivos](#manipulação-de-arquivos)
- [Bibliotecas](#bibliotecas)



---

# 📓 Meu aprendizado

### 📌Variáveis
> Variáveis são espaços  reservados  na  memória  do computador temporariamente para um determinado dado. 

```python
Variaveis.py

    nome = input("Digite um funcionário: ")
    empresa = input("Digite a instituição: ")
    qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
    mediaMensalidade = float(input("Digite a média da mensalidade: "))

    print(nome + " trabalha na empresa " + empresa)
    print("Possui: ", qtde_funcionarios, " funcionarios.")
    print("A média da mensalidade é de: " + str(mediaMensalidade))
    
    print("============== Verifique os tipos de dados abaixo: ==============")
    
    print("O tipo de dado da variavel [nome] é: ", type(nome))
    print("O tipo de dado da variavel [empresa] é: ", type(empresa))
    print("O tipo de dado da variavel [qtde_funcionarios] é: ", type(qtde_funcionarios))
    print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))
```

---


### 📌Tomadas de decisão
  As decisões direcionam caso a condição testada seja  `True` ou `False`. 
  
  Veja o exemplo de um mini programa para uma sala de emergência em um hospital:


```python
  nome = input("Digite o nome: ")
  idade = int(input('Digite a idade: ' ))
  doenca_infecctocontagiosa = input('Suspeita de doença infectocontagiosa?').upper()
  
  if idade >= 65:
      print('O paciente ' + nome + ' POSSUI atendimento prioritário!')
  elif doenca_infecctocontagiosa=="SIM":
      print('O paciente ' + nome + ' deve ser direcionado para a sala de espera de reserva.')
  else:
      print('O paciente ' + nome + ' NÃO possui atendimento prioritário e pode esperar na sala comum!')
```

> Console

```python
  >>> Digite o nome: Joao
  >>> Digite a idade: 69
  >>> Suspeita de doença infectocontagiosa?SIM
  >>> O paciente Joao POSSUI atendimento prioritário!
```
> Console

```python
  Digite o nome: Lucas
  Digite a idade: 45
  Suspeita de doença infectocontagiosa?NÃO
  O paciente Lucas NÃO possui atendimento prioritário e pode esperar na sala comum!
```

Há decisões compostas, encadeadas para ver mais exemplos de códigos [Clique aqui](https://github.com/CassiaXMS/codigos_Python/tree/master/Decisoes)

---

### 📌Laços de repetições

> Os laços de repetições servem para que uma ação seja repetida uma determinada ou indeterminada quantidade de vezes.

- **WHILE** - parece com o `if`, porém com a diferença que executará o bloco de código inúmera vezes enquanto não for falsa.

```python
numero=int(input("Digite um numero: "))
while numero<=100:
 print("" + str(numero))
 numero=numero+1
print("Laço encerrado...")
```

- **FOR** - geralmente usado quando você sabe o número de iterações necessárias para determinada operação.

```python
# EXERCICIO DA TABUADA

numero=int(input("Digite o numero: "))
print("Tabuada do numero:  " , numero)

for valor in range(1,11,1):
    print(str(numero) + " x " + str(valor) + " = " + str(numero*valor))
```

- Para o laço FOR criamos um variável denominada `numero`;
- em seguida uma função, o `range()` em que determina um faixa de valores a ser incrementada;
- `range(1)` significa que variável iniciará com valor 1, em seguida até o valor que o usuário digitar;
- por último ela será incrementada de 1 em 1.
  
---

### 📌Listas

> Listas são estrutura de dados que armazenam uma coleção ordenada de itens.
Elas são:
- **Versáteis:** armazenam `tipos` de dados diferentes (int, strings, float, ...)
- **Mutáveis:** podendo alterar, adicionar, excluir os elementos dinamicamente.
- **Índice:** manipulação dos elementos individuais por meio de índices.
- Além de possuir métodos embutidos, `append()`


```python
#lista preenchida estaticamente
lista_estatica = ["String", True]

#lista preenchida dinamicamente
lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado? ")))]

#lista vazia
lista_vazia=[]
```
> [!TIP]
> Quer mais exemplos de exercícios? Veja aqui!

A lista pode tornar ineficiente para operações de buscas, pois terá que percorrer todos os elementos (foreach)
tornando o desempenho comprometido em comparação com outras estruturas de dados como os dicionários (veremos à frente).

---

### 📌Funções

> Umas das suas vantagens é o **reaproveitamento de código e a modularização**, basicamente resolvemos o problema em partes, cada tarefa uma função.

No Python, o comando de função é `def`

```python

#Exemplo de uma função

def perguntar():
    return input("\n--- MENU ----\n" +
                 "<I> - Para Inserir um usuário\n" +
                 "<P> - Para Pesquisar um usuário\n" +
                 "<E> - Para Excluir um usuário\n" +
                 "<L> - Para Listar um usuário\n" +
                 "\n O que deseja realizar? ").upper()
```

O próximo passo é chamar as funções. Você pode criar um Python Package no Pycharm, contendo todas as funções que serão importadas.

Em seguida crie um novo arquivo importando através dos comando `from` (local físico das funções) `import *` (importar todas as funções).

> [!TIP]
> Ficou com alguma dúvida veja os exemplos.

---

### 📌Dicionários

**Quando utilizar a estrutura de dados Dicionários?**


 Dicionários armazenam objetos.

 Cada objeto será dividido em **chaves-dados**:

 - **chave** -  é justamente o identificador único do objeto.
 
 - **dados** - são os dados da chave.

 Como criar?
 
```python
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
```
> [!NOTE]
> Perceba que o login é a chave do dicionário usuarios, depois temos os dois-pontos(:) e os dados da chave.
No exemplo os dados são mais de um, então criamos um lista para armazenar esses dados.

---

### 📌Tuplas

> Também é uma Estrtura de Dados, porém com a diferença de não aceitar alteração sobre os dados já inseridos.

**Observações:** 

Geralmente aplica Tuplas para realizar a leitura de uma resposta no Python;

Pode ser utilizada como chave de um Dicionário;

Utilizada para retornar múltiplos valores.

---

### 📌Manipulação de arquivos

> Quando precisamos armazenar dados de forma persistente para que possam ser recuperados 
 mesmo após o fechamento e reabertura do sistema, os arquivos são uma opção comum 
 e poderosa em muitas linguagens de programação, incluindo Python.
 
Vejamosos modos de abertura de arquivos:

| Modo | Descrição |
| -- | -- |
| `w` | abrirá um arquivo de modo de escrita, caso o arquivo exista ele será sobrescrito. |
| `r` | abrirá o arquivo somente no modo leitura |
| `a` | ler e escrever além de ir adicionando conteúdo no arquivo |
| `x` | criar um novo arquivo em modo exclusivo |

Criando o primeiro arquivo:



```python
with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo")

with open("teste.txt", "a") as arquivo:
    arquivo.write("\nContinuação do texto.")
```


**Comentários:**

Utilizando o comando `WITH` o controle de encerramento ficará por conta dele
sem precisar do método close().

## Ficou curioso?

Veja um exemplo prático de manipulação de arquivos (txt, json, csv, html) para gerir um inventário de ativos de uma rede.
Veja também a manipulação de arquivos de terceiros

---


### 📌Bibliotecas 

Para utilizar pacotes externos no Python é preciso baixá-lo por meio do comando `pip install`.

- **Biblioteca Geopy** -  Converte um texto em coordenadas geográficas. Vejamos:

```python
# Aplicação

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

latitude=float(input("Digite a latitude...: "))
longitude=float(input("Digite a longitude.: "))

resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",")
if resultado[0]!='None':
    print("Endereço completo.: ", resultado)
    print("Dado 1............: ", resultado[0])
    print("Dado 2............: ", resultado[1])
    print("Dado 3............: ", resultado[2])

```

**Resultado:**

```python
Digite a latitude...: -22.900829520814703
Digite a longitude.:  -47.04478906756945
Endereço completo.:  ['Rua Arthur Bernardes', ' Nova Campinas', ' Campinas', ' Região Imediata de Campinas', 
' Região Metropolitana de Campinas', ' Região Geográfica Intermediária de Campinas', ' São Paulo', ' Região Sudeste', ' 13092-123', ' Brasil']
Dado 1............:  Rua Arthur Bernardes
Dado 2............:   Nova Campinas
Dado 3............:   Campinas

```


- `Biblioteca SOCKET`: estabelece comunicação em uma rede de computadores.
- `Biblioteca ftplib`: responsável pela manipulação do Protocolo de transferência de arquivos (FTP).
- `Pacote getpass`: solicitar ao usuário a entrada de uma senha de forma segura.
- `Biblioteca Serial`: realiza a comunicação serial com dispositivos externos (por exemplo, Arduino) por meio de portas seriais.

---

## 🛠 Ferramentas
- Python 3.12.1
- IDE PyCharm
---

## 📝 Autor

Este projeto está sobre a licença [MIT](./LICENSE).

Feito com ❤️ por Cassia Xavier 
👋🏽 Entre em contato!

<a href="https://www.linkedin.com/in/c%C3%A1ssia-xavier-mendes-dos-santos/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=flat-square&logo=linkedin&logoColor=white" target="_blank"></a>  
