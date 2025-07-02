# 🕹️ Game Store

## 📖 Descrição do Projeto

Este é um projeto full-stack que simula uma loja digital de jogos, inspirado em plataformas como Steam, GOG e Epic Games. O sistema permite a venda de jogos digitais, criação de contas, gerenciamento de pedidos, biblioteca do usuário e carteira virtual.

A aplicação está dividida em back-end (Django REST Framework) e front-end (React).


---

## ⚙️ Tecnologias Utilizadas

### 🔧 Back-end
- **Python**
- **Django**
- **Django REST Framework**
- **SQLite / PostgreSQL**
- **Poetry** (gerenciador de dependências)
- **JWT ou Token Auth (DRF Authtoken)** *(a definir)*
- **Docker (opcional)**

### 🎨 Front-end
- **React.js** *(em desenvolvimento)*
- **Axios**
- **React Router DOM**

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório:

```
git clone https://github.com/LPesposito/game-store
```
### 2. Back-end
```
cd backend
poetry install
poetry run python manage.py migrate
poetry run python manage.py runserver
```
Acesse: http://localhost:8000/

### 3. Front-end
```
cd frontend
npm install
npm start
```
Acesse: http://localhost:3000/

### 🧩 Estrutura do Projeto (Back-end)
| App         | Responsabilidade                                                             |
| ----------- | ---------------------------------------------------------------------------- |
| `product`   | Cadastro de jogos (produtos), categorias e imagens                           |
| `order`     | Pedidos de compra realizados pelos usuários                                  |
| `shop_cart` | Carrinho de compras antes de finalizar a compra                              |
| `wallet`    | Sistema de carteira digital com saldo, transações e gerenciamento financeiro |
| `library`   | Biblioteca de jogos comprados com chaves de acesso únicas                    |
| `user`      | Gerenciamento de usuários e autenticação (com possibilidade de customização) |


### 🔐 Segurança e Autenticação
- As rotas protegidas exigem autenticação por Token.

- As senhas são tratadas com hash seguro e transmitidas via HTTPS (quando em produção).

- Cada recurso sensível está vinculado ao request.user, garantindo integridade e privacidade.

### 📌 Funcionalidades Implementadas
### ✅ Básico
 - CRUD de produtos (jogos)

 - CRUD de categorias

 - Upload de imagens para os jogos

 - Sistema de usuários e autenticação com token

### 🛒 Loja
 - Adição de produtos ao carrinho

 - Finalização do pedido (Order)

 - Cálculo automático de total

 - Criação de OrderItem para múltiplos produtos

### 👛 Wallet
 - Carteira digital vinculada a cada usuário

 - Adição e retirada de saldo

 - Histórico de transações com timestamp

### 🎮 Biblioteca
 - Registro automático de produtos comprados

 - Geração de chave de acesso (access_key)

 - Visualização da biblioteca do usuário autenticado

### 🔁 Fluxo de Compra
   - A[Usuário] --> B[Adiciona produto ao carrinho]
   - B --> C[Checkout / Criar Order]
   - C --> D[Desconta saldo da Wallet]
   - C --> E[Cria LibraryEntry com access_key]

### 🧪 Testes
- Testes unitários com pytest e pytest-django

- Testes automatizados para:

   - Orders

   - Biblioteca

   - Wallet

   - Autenticação

   - Validação de permissões

### 🛠️ Em Desenvolvimento
 - Integração com front-end React

 - Validação de chaves de acesso (para simular download/autorização)

 - Painel de admin personalizado

 - Testes de integração

### 🤝 Contribuição
Contribuições são bem-vindas!
Abra uma issue ou envie um PR.

### 📄 Licença
Este projeto está sob a licença MIT.