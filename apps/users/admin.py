from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import User


# UserAdmin class with password change and reset
class UserAdmin(UserAdmin):
    list_display = ["email", "name", "username", "is_superuser"]
    search_fields = ["email", "name", "username"]
    list_filter = ["is_superuser", "is_active"]
    ordering = ["email"]
    filter_horizontal = []
    fieldsets = []
    add_fieldsets = []
    readonly_fields = ["created_at", "updated_at"]
    actions = []

    def get_fieldsets(self, request, obj=None):
        return (
            (None, {"fields": ("email", "password")}),
            ("Personal info", {"fields": ("name", "username", "bio", "website", "location", "birth_date")}),
            ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups")}),
            ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
        )

    def get_add_fieldsets(self, request, obj=None):
        return (
            (None, {"fields": ("email", "password1", "password2")}),
            ("Personal info", {"fields": ("name", "username", "bio", "website", "location", "birth_date")}),
            ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        )


admin.site.register(User, UserAdmin)
