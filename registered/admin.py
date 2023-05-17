from django.contrib import admin

from registered.models import Form


class AdminForm(admin.ModelAdmin):
    list_display=("id","first_name","last_name","date_of_birth","gender","class_","email","contact_number","item")

admin.site.register(Form,AdminForm)