# 📚 Game Store API - Documentação de Endpoints

## Autenticação

- **POST** `/api-token-auth/`  
  Autentica usuário e retorna token de acesso.
  - Body: `{ "username": "usuario", "password": "senha" }`
  - Response: `{ "token": "..." }`

---

## 🕹 Product

- **GET** `/api/product/`  
  Lista todos os produtos (jogos).

- **POST** `/api/product/`  
  Cria um novo produto (admin).

- **GET** `/api/product/{id}/`  
  Detalhes de um produto.

- **PUT/PATCH** `/api/product/{id}/`  
  Atualiza um produto (admin).

- **DELETE** `/api/product/{id}/`  
  Remove um produto (admin).

---

## 📦 Order

- **GET** `/api/order/`  
  Lista pedidos do usuário autenticado.

- **POST** `/api/order/`  
  Cria um novo pedido.

- **GET** `/api/order/{id}/`  
  Detalhes de um pedido.

- **POST** `/api/order/{id}/confirm/`  
  Confirma o pagamento do pedido.

---

## 🛒 Shop Cart

- **GET** `/api/shop-cart/`  
  Visualiza o carrinho do usuário.

- **PATCH/PUT** `/api/shop-cart/`  
  Atualiza itens do carrinho.

---

## 👤 User

- **POST** `/api/user/register/`  
  Cria um novo usuário.

- **GET** `/api/user/me/`  
  Detalhes do usuário autenticado.

- **PUT/PATCH** `/api/user/me/`  
  Atualiza dados do usuário autenticado.

---

## 💰 Wallet

- **GET** `/api/wallet/`  
  Consulta saldo da carteira.

- **POST** `/api/wallet/deposit/`  
  Realiza depósito na carteira.

- **GET** `/api/wallet/transactions/`  
  Lista transações da carteira.

---

## 🎮 Library

- **GET** `/api/library/`  
  Lista jogos adquiridos pelo usuário.

---

> **Obs:**  
- Todos os endpoints (exceto registro/login) exigem autenticação via token.
- Para testar, envie o header: `Authorization: Token <seu_token>`

---

**Adapte conforme os detalhes reais das suas rotas e regras!**