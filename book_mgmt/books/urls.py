from django.urls import path

from books.views import HomePageView

app_name = "books"

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name="homepage"),
]