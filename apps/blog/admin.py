from django.contrib import admin

# Register your models here.
# from . models import Book, Article, Author, User, Comment


## A way to register several models
## Just add new model to the list
from .models import *

@admin.register(Book, Article, Author, User, Comment)
class BlogAdmin(admin.ModelAdmin):
    pass


# admin.site.register(Book)
# admin.site.register(Article)
# admin.site.register( Author)