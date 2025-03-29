# 🚀 API de Gerenciamento de Tarefas (To-Do List)

API desenvolvida com Django e Django REST Framework para o desafio backend da Labens.

## 📋 Requisitos do Projeto

- CRUD completo de tarefas
- Paginação (5 itens por página)
- Busca em título e descrição
- Filtros por status e data
- Testes unitários
- Docker (opcional)

## 🛠 Tecnologias Utilizadas

- Python 3.9+
- Django 4.0+
- Django REST Framework
- SQLite (banco padrão)
- Docker (containerização opcional)

## ⚙️ Configuração do Ambiente

### Pré-requisitos

- Python 3.9+
- Pipenv ou virtualenv
- Docker (opcional)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/todo-api.git
cd todo-api

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Popule o banco de dados (opcional)
python manage.py populate_tasks

# Inicie o servidor
python manage.py runserver

# Rodar Testes
python manage.py test

# Com Docker
docker-compose up --build
```

# Execute os containers

docker-compose up
