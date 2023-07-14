Documentation
https://www.django-rest-framework.org/topics/documenting-your-api/
https://git.icm.edu.pl/kriestof/django-rest-swagger/-/blob/79ec33031a35ce164b847257c09321896f038bde/README.md

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