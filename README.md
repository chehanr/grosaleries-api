# GroSaleries-api

API service for the SWE20001 project (GroSaleries).

## Requirements

- Python 3.7.x
- PostgreSQL

## Installation

    git clone https://github.com/nguyenhailong253/back_end.git && cd tutreq
    virtualenv ENV
    ENV/Scripts/activate
    pip install -r requirements.txt

Rename `.env.sample` to `.env` and provide the variables.

    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py runserver

## Deploying to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/nguyenhailong253/back_end)

- Set the necessary environment variables.
- Run the above mentioned Django commands.