Installation
============

* Download and install latest version of `Django Log Reader`_:

.. code-block:: console

    $ pip install django-log-reader

Setup
-------

* Add ``log_reader`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        "log_reader.apps.LogReaderConfig",
    )

* You can Add the following value In your ``settings.py`` file:

.. code-block:: python

    # This value specifies the folder for the files. The default value is 'logs'
    LOG_READER_DIR_PATH = 'logs'

    # This value specifies the file extensions. The default value is '*.log'
    LOG_READER_FILES_PATTERN = '*.log'

    # This value specifies the default file. If there is no filter, the system reads the default file.
    LOG_READER_DEFAULT_FILE = 'django.log'

    # The contents of the files are separated based on this pattern.
    LOG_READER_SPLIT_PATTERN = "\\n"

    # This value indicates the number of lines of content in the file. Set the number of lines you want to read to this value.
    LOG_READER_MAX_READ_LINES = 1000

    # You can exclude files with this value.
    LOG_READER_EXCLUDE_FILES = []


* Collect static if you are in production environment:

.. code-block:: console

    $ python manage.py collectstatic

* Clear your browser cache


.. _Django Log Reader: https://pypi.org/project/django-admin-two-factor/
