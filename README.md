# Book-Management

# Installation

`virtualenv env`

# For Mac/ Linux

`source env/bin/activate`

# For Window

`env\scripts\activate`

# Commands

Inside env install requirements

`pip install -r requirements.txt`   

OR, install Django, Pillow, psycopg2-binary

# Django Commands

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

You can create requirements.txt using command:

`pip freeze > requirements.txt`


Create a .env file to hide your secret keys and other vital informations, and use config to use in settings file

Your .env file will look something like this:

ENVIRONMENT_TYPE=development

```
    SECRET_KEY=<your secret key>
    DB_ENGINE=django.db.backends.postgresql_psycopg2
    DB_NAME=book_mgmt
    DB_USER=<db_user>
    DB_PASSWORD=<db_pwd>
    DB_HOST=127.0.0.1
    DB_PORT=5432

```
