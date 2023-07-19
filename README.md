install poetry - https://python-poetry.org/docs/#installing-with-the-official-installer
poetry shell to go env
poetry install to install the dependencies
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt