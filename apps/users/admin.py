from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active')
    search_fields = ('username', 'email')
    list_filter = ('is_active',)
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'date_of_birth', 'mobile_number', 'country')}),
        ('Permissions', {'fields': ('is_active',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active')}
        ),
    )

admin.site.register(User, CustomUserAdmin)
