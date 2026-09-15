# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a criar uma API REST com FastAPI, definindo rotas, validando dados com modelos Pydantic e retornando respostas HTTP apropriadas. Ao final, você terá uma pequena API de tarefas com operações de consulta, criação e atualização.

## 📝 Tasks

### 🛠️ Create Your First API Endpoint

#### Descrição
Complete a aplicação inicial para criar um endpoint de verificação de saúde da API. Execute o servidor localmente e confirme que a rota retorna JSON.

#### Requisitos

- Criar uma aplicação FastAPI no arquivo `starter-code.py`
- Implementar um endpoint `GET /health`
- Retornar `{"status": "ok"}` com status HTTP `200`
- Iniciar a aplicação com Uvicorn e testar a rota em `/docs`

### 🛠️ Build a Task Resource

#### Descrição
Transforme a aplicação em uma API de tarefas usando um armazenamento em memória. Defina um modelo de entrada para garantir que os dados recebidos tenham o formato correto.

#### Requisitos

- Criar um modelo Pydantic `TaskCreate` com os campos `title` e `completed`
- Implementar `GET /tasks` para retornar todas as tarefas
- Implementar `POST /tasks` para criar uma tarefa e retornar status HTTP `201`
- Atribuir um `id` inteiro único para cada tarefa criada
- Rejeitar requisições sem título ou com um tipo inválido para `completed`

### 🛠️ Add Update and Error Handling

#### Descrição
Adicione operações para consultar e atualizar uma tarefa específica. A API deve comunicar claramente quando o recurso solicitado não existe.

#### Requisitos

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa pelo ID
- Implementar `PUT /tasks/{task_id}` para atualizar `title` e `completed`
- Retornar status HTTP `404` quando o ID não existir
- Usar `HTTPException` para produzir respostas de erro consistentes
- Demonstrar as rotas implementadas com pelo menos três exemplos de requisições no Swagger em `/docs`