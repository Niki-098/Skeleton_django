from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ('email', 'name', 'date_joined', 'last_login')
    list_filter = ('date_joined',)
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()

    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('last_login',)}),
        ('Important dates', {'fields': ('date_joined',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
