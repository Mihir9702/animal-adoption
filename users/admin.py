from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_active', 'is_admin')
    list_filter = ('is_active', 'is_admin')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_admin'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    # Remove or modify the filter_horizontal attribute
    filter_horizontal = ()  # or remove this line if not needed

admin.site.register(CustomUser, CustomUserAdmin)
