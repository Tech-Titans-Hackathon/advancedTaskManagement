from django.contrib import admin
from .models import Task, TaskAssignment

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'assigned_to', 'status')
    search_fields = ('name', 'project', 'assigned_to')
    list_filter = ('status',)

@admin.register(TaskAssignment)
class TaskAssignmentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'assigned_at')
    search_fields = ('task__name', 'user__username')
    list_filter = ('assigned_at',)