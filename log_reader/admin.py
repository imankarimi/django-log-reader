import django
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from log_reader import settings
from log_reader.models import FileLogReader
from log_reader.utils import get_log_files, read_file_lines


@admin.register(FileLogReader)
class FileLogReaderAdmin(admin.ModelAdmin):
    list_filter = ['id']

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.module_name
        return [
            path(r'', self.admin_site.admin_view(self.changelist_view), name='%s_%s_changelist' % info),
        ]

    def changelist_view(self, request, extra_context=None):
        filename = request.GET.get('file_name', settings.LOG_READER_DEFAULT_FILE)

        is_valid, file_contents = read_file_lines(
            file_name=filename)
        log_files = get_log_files(settings.LOG_READER_DIR_PATH)

        context = dict(
            self.admin_site.each_context(request),
            log_files=log_files,
            file_contents=file_contents,
            file_name=filename,
            django_version=django.get_version()
        )
        return TemplateResponse(request, "log_reader/admin/change_list.html", context=context)
