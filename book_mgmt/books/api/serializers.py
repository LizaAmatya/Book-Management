
from books.models import Author, Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        
    # def validate(self, obj):
    #     ...


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
