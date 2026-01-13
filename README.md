# Lista de Tarefas

## Descrição

Esse projeto é um aplicativo feito em Python que serve para gerenciar tarefas.
Com ele é possível adicionar, listar, excluir e mudar o status das tarefas.
O projeto foi feito para a avaliação 3 de Engenharia de Software.

---

## Funcionalidades

* Adicionar tarefa (nome, descrição e status)
* Listar todas as tarefas
* Listar tarefas por status
* Alterar o status de uma tarefa
* Excluir tarefa

Os status possíveis são: **Disponível**, **Fazendo** e **Feito**.

---

## Padrões de Projeto Usados

**Singleton**

* Usado na classe `ControladorTarefas`.
* Garante que só exista um controlador que gerencia todas as tarefas.

**Factory**

* Usado na classe `FabricaStatus`.
* Cria o status da tarefa de acordo com a escolha do usuário.
* Substitui vários `if` repetidos e deixa o código mais organizado e fácil de manter.

---

## Como Rodar

1. Instale o **Python** no seu computador.
2. Baixe ou clone o repositório:

   ```
   git clone https://github.com/hissa02/lista-de-tarefas.git
   ```
3. Abra a pasta do projeto no terminal:

   ```
   cd lista-de-tarefas
   ```
4. Execute o programa principal:

   ```
   python main.py
   ```
