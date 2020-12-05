from django.contrib import admin
from home import models

class BooksAdmin(admin.ModelAdmin):
    list_display = ("bookName","authorName","price","descr")
    search_fields = ("bookName","authorName")

admin.site.register(models.Books,BooksAdmin)
# Register your models here.
