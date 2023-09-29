# Simplify To-Do
Repositório para desenvolvimento do Simplify To-DO. Gereciador de Tarefas cuja finalidade é seer um desafio técnico à vaga de Desenvolvedor Fullstack Liferay da Simplify.

## Descrição
- Desenvolva uma aplicação web utilizando uma linguagem de programação e um framework de sua escolha. A aplicação deve consistir em um sistema de gerenciamento de tarefas, onde os usuários podem criar, visualizar, editar e excluir tarefas.

## Requisitos
- Usar banco de dados relacional
- Campos mínimos da entidade de tarefa
    - Nome
    - Descrição
    - Realizado
    - Prioridade
    - Data de criação
- Criar CRUD de tarefas
- Deve ser possível mudar a ordem das tarefas por meio de _drag and drop_
- (Opcional) Desenvolver aplicação dentro de um container Docker ou hospedar ela publicamente

## Instruções
- Fazer um fork do repositório para sua conta pessoal do git
- Trabalhar utilizando commits
- Documentar como executar sua aplicação
- Descrever as funcionalidades do software

## Gerenciamento de Tarefas:
- Realizado por Issues.

## Instalação 

### Requisitos
* Docker 
* Docker Compose

### Como instalar

1 - Clone o repositório

2 - Entre na pasta do projeto

3 - Rode o comando:
```
sudo docker-compose up
```

4 - Acesse localhost:8003


Para acessar o container da aplicação use o seguinte comando:
```
sudo docker exec -it desafio-fullstack-web-1 bash
```

Para ver todos os containers rodando na sua máguina use o seguinte comando:

```
sudo docker ps
```

