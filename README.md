## Instalação

Primeiro, crie um ambiente virtual.
Com seu ambiente virtual configurado, instale as dependências do projeto com:

```bash
pip install -r requirements.txt
```

Para criar as _Migrations_:

```bash
python manage.py makemigrations
```

Para efetivar as _Migrations_ no banco de dados:

```bash
python manage.py migrate
```

## Execução

Para executar o servidor de testes do Django, execute:

```bash
python manage.py runserver


##Para acessar a página Admin:
user: admin / password: 101001
