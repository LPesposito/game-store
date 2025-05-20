FROM python:3.12-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y curl build-essential

# Instala o Poetry
ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -

# Adiciona poetry no PATH
ENV PATH="/root/.local/bin:$PATH"

# Cria diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY pyproject.toml poetry.lock ./

# Desabilita criação de virtualenv e instala dependências principais
RUN poetry config virtualenvs.create false && poetry install --only main

# Copia o restante do código
COPY . .

RUN poetry run python manage.py makemigrations
RUN poetry run python manage.py migrate
# Expõe porta da aplicação
EXPOSE 8000

# Comando para rodar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]