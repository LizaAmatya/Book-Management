from django.urls import path

from books.views import BookCreateView, BookListView, BookUpdateView, HomePageView

app_name = "books"

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name="homepage"),
    path('', BookListView.as_view(), name="book_list"),
    path('create/', BookCreateView.as_view(), name="book_create"),
    path('update/<int:pk>/', BookUpdateView.as_view(), name="book_update")
]
