# game-store

## Descrição do Projeto

Este é um projeto de Back-end desenvolvido para gerenciar uma loja de jogos. Ele fornece funcionalidades para cadastro, consulta, atualização e exclusão de informações relacionadas a jogos, clientes e pedidos.

## Tecnologias Utilizadas

- Django Rest Framework
- Python
- Banco de Dados (ex.: PostgreSQL, SQLite, etc.)
- Poetry para gerenciamento de dependências
- Outras ferramentas e bibliotecas relevantes

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/LPesposito/game-store
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

7. O servidor estará disponível em `http://localhost:8000` (ou na porta configurada).

## Funcionalidades

- Gerenciamento de jogos (CRUD)
- Gerenciamento de clientes (CRUD)
- Gerenciamento de pedidos (CRUD)

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
