from django.conf import settings


""" log reader config """

LOG_READER_DIR_PATH = getattr(settings, 'LOG_READER_DIR_PATH', 'logs')
LOG_READER_FILES_PATTERN = getattr(settings, 'LOG_READER_FILES_PATTERN', '*.log')
LOG_READER_DEFAULT_FILE = getattr(settings, 'LOG_READER_DEFAULT_FILE', 'django.log')
LOG_READER_SPLIT_PATTERN = getattr(settings, 'LOG_READER_SPLIT_PATTERN', "\\n")
# The contents of the files are separated based on this regex. if it couldn't split correctly with both pattern.
# The default value is '[(?i)[0-9]{4}-[0-9]{2}-[0-9]{2}\\s(?:[0-9]{2}:){2}[0-9]{2}.+?(?=[0-9]{4}-[0-9]{2}-[0-9]{2}\\s(?:[0-9]{2}:){2}[0-9]{2}|$)'
LOG_READER_REGEX_SPLIT_PATTERN = '[(?i)[0-9]{4}-[0-9]{2}-[0-9]{2}\\s(?:[0-9]{2}:){2}[0-9]{2}.+?(?=[0-9]{4}-[0-9]{2}-[0-9]{2}\\s(?:[0-9]{2}:){2}[0-9]{2}|$)'
LOG_READER_MAX_READ_LINES = getattr(settings, 'LOG_READER_MAX_READ_LINES', 1000)
LOG_READER_EXCLUDE_FILES = getattr(settings, 'LOG_READER_EXCLUDE_FILES', [])

