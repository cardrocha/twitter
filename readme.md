# PROJETO TWITTER

### Instalando as dependências
```
pip install -r requirements.txt
```
### Execução
Criando Migração

```
poetry run python manage.py makemigrations
```
Sincronizando com banco de dados
```
poetry run python manage.py migrate
```
Criar um superusuário com privilégios administrativos
```
poetry run python manage.py createsuperuser
```

Inicia o servidor
```
poetry run python manage.py runserver
```