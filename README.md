# Django Log Reader
**Django Log Reader** allows you to read &amp; download log files on the admin page for *Linux* os.

:warning: **Warning!!**
* This version is designed for the Linux operating system and uses Linux commands to read files faster.

<br />

## Why Django Log Reader?

- Reading files based on Linux commands speeds up the display of file content
- Download the result of the content
- Display all files according to the pattern defined in the `settings.py`
- Simple interface
- Easy integration

<br>

## How to use it

<br />

* Download and install latest version of Django Log Reader:

```bash
$ pip install git+https://github.com/imankarimi/django-log-reader.git
// OR
$ easy_install git+https://github.com/imankarimi/django-log-reader.git
```

<br />

* Add `log_reader` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file:

```python
INSTALLED_APPS = (
    # ...
    'log_reader.apps.LogReaderConfig',
)
```

<br />

* Collect static if you are in production environment:
```bash
$ python manage.py collectstatic
```

* Clear your browser cache

<br />

## Start the app

```bash
$ # Set up the database
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Create the superuser
$ python manage.py createsuperuser
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
```

* Access the `admin` section in the browser: `http://127.0.0.1:8000/`
