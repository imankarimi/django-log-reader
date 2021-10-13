Run & Demo
##############

Run
-----

.. code-block:: console

    # Set up the database
    $ python manage.py makemigrations
    $ python manage.py migrate

    # Create the superuser
    $ python manage.py createsuperuser

    # Start the application (development mode)
    $ python manage.py runserver # default port 8000

Access the ``admin`` section in the browser: ``http://127.0.0.1:8000/``

Demo
------

.. image:: https://raw.githubusercontent.com/imankarimi/django-log-reader/main/screenshots/django_log_reader.png
    :alt: Demo
