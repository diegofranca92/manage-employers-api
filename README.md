install poetry - https://python-poetry.org/docs/#installing-with-the-official-installer
poetry shell to go env
poetry install to install the dependencies
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

Documentation
https://www.django-rest-framework.org/topics/documenting-your-api/
https://git.icm.edu.pl/kriestof/django-rest-swagger/-/blob/79ec33031a35ce164b847257c09321896f038bde/README.md

https://www.youtube.com/playlist?list=PL6u1VNwqZdJZT5lCMbBQA1UHVWy0FOYOl
https://www.youtube.com/@RegisdoPython/playlists

manager_user
minhasenha1
common_user
minhasenha2

TO RUN:
- Configure your venv:
  ```
    $ virtualenv  venv -p python3
    $ source venv/bin/activate
  ```
- Install the dependencies needed to run the app:

   ```
     $ pip install -r requirements.txt
   ```
- Make those migrations work:
  ```
    $ python3 manage.py makemigrations
    $ python3 manage.py migrate
  ```
- Create Superuser to acess the Django admin:
  ```
    $ python3 manage.py createsuperuser
  ```
- Fire up the server:
  ```
    $ python3 manage.py runserver
  ```
- Open in Browser to view server:
  http://127.0.0.1:8000/admin