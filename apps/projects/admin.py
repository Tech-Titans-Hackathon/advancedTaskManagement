from django.contrib import admin
from .models import Project, ProjectMember

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    # list_filter = ('start_date', 'end_date', 'created_at')
    
@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'role')
    search_fields = ('project__name', 'user__username')
    list_filter = ('role',)