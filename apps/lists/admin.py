from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Category, Item, Fellowship)
class ListsAdmin(admin.ModelAdmin):
    pass