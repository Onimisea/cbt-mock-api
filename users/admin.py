from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("fullname", "jamb_reg_num", "generated_password", "password")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("fullname", "jamb_reg_num", "generated_password", "password1", "password2"),
            },
        ),
    )

    list_display = ("fullname", "jamb_reg_num", "generated_password", "is_staff", "last_login")

    ordering = ('jamb_reg_num',)

admin.site.register(User, UserAdmin)
