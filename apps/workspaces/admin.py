from django.contrib import admin
from .models import Workspace,WorkspaceMember 

@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')  # Customize as needed
    search_fields = ('name',)

@admin.register(WorkspaceMember)
class WorkspaceMemberAdmin(admin.ModelAdmin):
    list_display = ('workspace', 'user', 'role')
    search_fields = ('workspace__name', 'user__username')
    list_filter = ('role',)