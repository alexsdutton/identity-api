# Identity API

A prototypical identity API supporting:

* Names (and not just first/last)
* Nationalities
* Affiliations and roles
* Gender
* Source documents, and the personal information they attest
* Publishing data changes to AMQP


# Getting started

Make rabbitmq available on localhost with a `guest:guest` administrator account.

    mkvirtualenv oxidentity --python=/usr/bin/python3
    pip install -r requirements

    createdb oxidentity
    django-admin.py migrate

    # Set a celery worker going
    celery -B -A oxidentity worker -l info &

    # Run the dev server
    django-admin.py runserver

    # Create a new person
    curl http://localhost:8000/person/ -d@examples/lewis-carroll.json -v