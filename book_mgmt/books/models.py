from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    published_date = models.DateField(null=True, blank=True)
    price = models.FloatField(null=False, blank=False)
    author = models.ForeignKey(Author, related_name='book_author', on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(null=True, blank=True)

     