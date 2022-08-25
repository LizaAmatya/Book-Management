
from books.models import Author, Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
        
        
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'name', 'published_date', 'price', 'author', 'cover_image']
        # depth = 1
        
  


class BookDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    # author_name = serializers.SerializerMethodField()
    
    
    class Meta:
        model = Book
        fields = ['id', 'name', 'published_date',
            'price', 'author', 'cover_image',
            # 'author_name'
            ]
        
    def get_author(self, obj):
        return AuthorSerializer(obj.author).data

    # def get_author_name(self, obj):
    #     return obj.author.name

