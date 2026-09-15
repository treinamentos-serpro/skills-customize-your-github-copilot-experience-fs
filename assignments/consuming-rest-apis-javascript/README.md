# 📘 Assignment: Consuming REST APIs with JavaScript

## 🎯 Objective

Aprenda a consumir uma API REST no navegador usando JavaScript nativo, `fetch`, JSON e manipulação do DOM. Ao final, você terá uma página que lista tarefas, cria novas tarefas e informa ao usuário quando uma requisição falha.

## 📝 Tasks

### 🛠️ Fetch and Display Tasks

#### Descrição
Conecte a página à API de tarefas criada na assignment de FastAPI. Use `fetch` para buscar os dados e mostre cada tarefa na lista da página.

#### Requisitos

- Fazer uma requisição `GET` para `/tasks`
- Converter a resposta para JSON
- Exibir o título e o estado de conclusão de cada tarefa
- Mostrar uma mensagem quando não houver tarefas
- Manter a interface funcional sem usar bibliotecas externas

### 🛠️ Create a New Task

#### Descrição
Adicione um formulário que envie uma nova tarefa para a API quando o usuário o preencher. Depois do envio, atualize a lista exibida no navegador.

#### Requisitos

- Adicionar um campo obrigatório para o título
- Adicionar um controle para indicar se a tarefa está concluída
- Fazer uma requisição `POST` para `/tasks` com um corpo JSON
- Enviar o cabeçalho `Content-Type: application/json`
- Recarregar a lista depois de uma criação bem-sucedida
- Limpar o formulário após o envio

Exemplo de corpo enviado:

```json
{
  "title": "Revisar fetch",
  "completed": false
}
```

### 🛠️ Handle Loading and Errors

#### Descrição
Melhore a experiência da página informando quando uma operação está em andamento e explicando os erros retornados pela API.

#### Requisitos

- Mostrar um estado de carregamento durante as requisições
- Verificar `response.ok` antes de usar a resposta como sucesso
- Exibir uma mensagem clara quando a API retornar um erro HTTP
- Tratar falhas de conexão com um bloco `catch`
- Desabilitar o botão de envio enquanto o formulário estiver sendo processado
- Permitir que o usuário tente novamente depois de um erro