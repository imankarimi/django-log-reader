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

<br />

![Django Log Reader](https://raw.githubusercontent.com/imankarimi/django-log-reader/main/screenshots/django_log_reader.png)


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

* You can Add the following value In your `settings.py` file.
```python
# This value specifies the folder for the files. The default value is 'logs'
LOG_READER_DIR_PATH = 'logs'

# This value specifies the file extensions. The default value is '*.log'
LOG_READER_FILES_PATTERN = '*.log'

# This value specifies the default file. If there is no filter, the system reads the default file.
LOG_READER_DEFAULT_FILE = 'django.log'

# The contents of the files are separated based on this value. Which is of the regex type.
# The default value is '[(?i)[0-9]{4}-[0-9]{2}-[0-9]{2}\\s(?:[0-9]{2}:){2}[0-9]{2}.+?(?=[0-9]{4}-[0-9]{2}-[0-9]{2}\\s(?:[0-9]{2}:){2}[0-9]{2}|$)'
LOG_READER_REGEX_SPLIT_PATTERN = '[(?i)[0-9]{4}-[0-9]{2}-[0-9]{2}\\s(?:[0-9]{2}:){2}[0-9]{2}.+?(?=[0-9]{4}-[0-9]{2}-[0-9]{2}\\s(?:[0-9]{2}:){2}[0-9]{2}|$)'

# This value indicates the number of lines of content in the file. Set the number of lines you want to read to this value.
LOG_READER_MAX_READ_LINES = 1000
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
