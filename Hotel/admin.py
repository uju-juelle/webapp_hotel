from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register([Products, Category, Reviews, Staff])

class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message"]

admin.site.register(Contact, ContactAdmin)