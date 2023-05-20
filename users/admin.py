from django.contrib import admin

from .models import SignedupUser


class UserAdmin(admin.ModelAdmin):
    list_display=("name",)

admin.site.register (SignedupUser,UserAdmin)
