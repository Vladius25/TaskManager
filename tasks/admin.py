from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from tasks.models import Task, Status


class TasksAdmin(SimpleHistoryAdmin):
    readonly_fields = ["creation_date", ]


admin.site.register(Task, TasksAdmin)
admin.site.register(Status)
