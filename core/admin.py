from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.utils.translation import gettext as _
from .models import User


@admin.register(User)
class UserAdmin(BaseAdmin):
  
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2","phonenumber"),
            },
        ),
    )

from djoser.serializers import UserSerializer