from django.contrib import admin

from .models import ShortifyURL


@admin.register(ShortifyURL)
class ShortifyURLAdmin(admin.ModelAdmin):
    list_display = ("id", "slug", "url", "user", "created", "modified")
    search_fields = ("slug", "user__email", "user__full_name")
    readonly_fields = ("slug", "created", "modified")
