from django.contrib import admin
from user.models import Myuser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django.db import models

# Register your models here.

class UserAdminConfig(UserAdmin):
    model = Myuser
    search_fields = ('email', 'first_name',)
    list_filter = ('email', 'first_name', 'is_active', 'is_staff')
    ordering = ('Created_at',)
    list_display = ('email', 'id', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(Myuser, UserAdminConfig)