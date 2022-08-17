from django.contrib import admin

from books.models import Author, Book

# Register your models here.
# @register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['name']
    
admin.site.register(Book)
admin.site.register(Author)