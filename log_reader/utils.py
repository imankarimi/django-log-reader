from __future__ import unicode_literals

import os
import re
import subprocess
from fnmatch import fnmatch

from log_reader import settings


def get_log_files(directory):
    for (dir_path, dir_names, filenames) in os.walk(directory):
        log_files = []
        all_files = list(filter(lambda x: x.find('~') == -1, filenames))
        log_files.extend([x for x in all_files if fnmatch(x, settings.LOG_READER_FILES_PATTERN)])
        return list(set(log_files))
    return []


def read_file_lines(file_name):
    try:
        file_path = '%s/%s' % (settings.LOG_READER_DIR_PATH, file_name)
        result = subprocess.run(
            ['tail', '-%s' % settings.LOG_READER_MAX_READ_LINES, file_path],
            capture_output=True,
            # text=True,
            encoding="utf8",
        )
        content = repr(result.stdout) if result.stdout else None
    except Exception as e:
        return False, str(e)

    return True, split_file_content(content)


def split_file_content(content):
    res = content.split(settings.LOG_READER_SPLIT_PATTERN) if content else []
    # if content and len(res) == 1:
    #     res = re.findall(settings.LOG_READER_REGEX_SPLIT_PATTERN, content) if content else []
    return res

