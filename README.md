# game-store

## Descrição do Projeto

Este é um projeto Full Stack para gerenciar uma loja de jogos, com back-end em Django Rest Framework e front-end moderno. O sistema permite cadastro, consulta, atualização e exclusão de informações relacionadas a jogos, clientes e pedidos.

## Tecnologias Utilizadas

- **Back-end**
  - Django Rest Framework
  - Python
  - Banco de Dados (ex.: PostgreSQL, SQLite, etc.)
  - Poetry para gerenciamento de dependências

- **Front-end**
  - [Adicione aqui o framework/biblioteca, ex.: React, Vue, Angular]
  - [Outras ferramentas relevantes do front-end]

## Como Executar o Projeto

### 1. Clone este repositório:
```bash
git clone https://github.com/LPesposito/game-store
```

---

### 2. Back-end

1. Acesse a pasta do back-end:
   ```bash
   cd backend
   ```

2. Instale o Poetry, caso ainda não tenha:
   ```bash
   pip install poetry
   ```

3. Instale as dependências:
   ```bash
   poetry install
   ```

4. Configure as variáveis de ambiente no arquivo `.env`.

5. Execute as migrações do banco de dados:
   ```bash
   poetry run python manage.py migrate
   ```

6. Inicie o servidor:
   ```bash
   poetry run python manage.py runserver
   ```

O back-end estará disponível em `http://localhost:8000`.

---

### 3. Front-end

1. Acesse a pasta do front-end:
   ```bash
   cd frontend
   ```

2. Instale as dependências (exemplo para projetos Node.js):
   ```bash
   npm install
   # ou
   yarn install
   ```

3. Inicie o servidor de desenvolvimento:
   ```bash
   npm start
   # ou
   yarn start
   ```

O front-end estará disponível em `http://localhost:3000` (ou na porta configurada).

---

## Funcionalidades **#WIP**

- Gerenciamento de jogos (CRUD)
- Gerenciamento de clientes (CRUD)
- Gerenciamento de pedidos (CRUD)
- Interface web amigável para interação com a API

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
