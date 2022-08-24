from django.urls import path

from .views import BookListAPIView

app_name = "api_books"

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list')
]