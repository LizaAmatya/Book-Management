from django.urls import path

from books.views import BookListView, HomePageView

app_name = "books"

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name="homepage"),
    path('', BookListView.as_view(), name="book_list"),
    
]