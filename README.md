

 Estou utilizando o gerenciador de pacotes **Poetry** [clique aqui](https://python-poetry.org/docs/#installing-with-the-official-installer) para instalar.

```shell
# Pra ativar o venv do Python
poetry shell

# Pra instalar as dependências do Projeto
poetry install

# Criar/Atualizar as migrations
python manage.py makemigrations

# Executar as migrations
python manage.py migrate

# Rodar o servidor Django
python manage.py runserver

```


> **Depois disso só abrir o navegador na documentação:**
>
> _Swagger_
> - http://127.0.0.1:8000/api/docs/swagger/
>
> _Redoc_
> - http://127.0.0.1:8000/api/docs/redoc/


<!-- 
poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt 

-->


<!-- 
Documentation
https://www.django-rest-framework.org/topics/documenting-your-api/
https://git.icm.edu.pl/kriestof/django-rest-swagger/-/blob/79ec33031a35ce164b847257c09321896f038bde/README.md

https://www.youtube.com/playlist?list=PL6u1VNwqZdJZT5lCMbBQA1UHVWy0FOYOl
https://www.youtube.com/@RegisdoPython/playlists

-->




<!-- 
manager_user
minhasenha1
common_user
minhasenha2

TO RUN:
- Configure your venv:
  ```shell
    $ virtualenv  venv -p python3
    $ source venv/bin/activate
  ```
- Install the dependencies needed to run the app:

   ```shell
     $ pip install -r requirements.txt
   ```
- Make those migrations work:
  ```shell
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
  ```
- Create Superuser to acess the Django admin:
  ```shell
    $ python3 manage.py createsuperuser
  ```
- Fire up the server:
  ```shell
    $ python3 manage.py runserver
  ```
- Open in Browser to view server:
  http://127.0.0.1:8000/admin -->