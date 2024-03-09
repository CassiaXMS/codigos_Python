<h1 align="center">
    <a>🔗 Introduction to Python </a>
</h1>

<h4 align="center"> 
	🚧 Concluído  🚧
</h4>

---
## 🏷️ Conteúdo

- [Variaveis](#variaveis)
- [Decisão](#decisao)
- [Laço de repeticao](#laco-de-repeticao)

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
  
  Veja o exemplo de um código para uma sala de emergêencia em um hospital:


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
