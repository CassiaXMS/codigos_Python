<h1 align="center">
    <a>🔗 Introduction to Python 🐍</a>
	
</h1>

> [!NOTE]
>  Parte destas anotações é baseada no [curso online de Python da Faculdade FIAP](https://on.fiap.com.br/local/nanocourses/index.php)

**Resumo:** Python é uma linguagem livre, multiparadigma, híbrida (compilada e interpretada), alto nível.
Linguagem simples para aprender e muito utilizada no mundo de segurança da informação.

---
## 🏷️ Conteúdo

- [Variaveis](#variaveis)
- [Decisão](#decisao)
- [Laço de repeticao](#laco-de-repeticao)
- [Listas](#Listas)
- [Funções](#funcoes)
- [Módulos](#modulos)
- [Dicionário](#dicionario)
- [Tuplas](#tuplas)

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
  As decisões direcionam caso a condição testada é  `True` ou `False`. 
  
  Veja o exemplo de um código para uma sala de emergência em um hospital:


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

Há decisões compostas, encadeadas para ver mais exemplos de códigos 

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

- **FOR** - parece com o `if`, porém com a diferença que executará o bloco de código inúmera vezes enquanto não for falsa.

```python
# EXERCICIO DA TABUADA

numero=int(input("Digite o numero: "))
print("Tabuada do numero:  " , numero)

for valor in range(1,11,1):
    print(str(numero) + " x " + str(valor) + " = " + str(numero*valor))
```

- Para o laço FOR criamos um variável denominada `numero`;
- em seguida uma função, o `range()` em que determina um faixa de valores a ser incrementada;
- `range(1)` significa que variável iniciará com valor 1 em seguida até o valor que o usuário digitar;
- por último ela será incrementada de 1 em 1.
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
