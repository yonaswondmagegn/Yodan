from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from django.utils.translation import gettext as _
from .models import User,AuthVerification


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
    list_display = ('phonenumber', 'is_staff', 'is_superuser',"is_active")

admin.site.register(AuthVerification)