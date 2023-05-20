from django.contrib import admin

# Register your models here.
from todo_api.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "due_date", "description", "created_at"]
    list_filter = ["status"]
