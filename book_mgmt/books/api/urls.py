from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import AuthorViewSet, BookCreateAPIView, BookListAPIView, BookUpdateAPIView

app_name = "api_books"

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')

'''
Using DefaultRouter and Viewset it provides following urls by default: using above author example:

  METHOD  URL       API 

# GET: 'authors/' -> list API 
# GET: 'authors/<int:pk>/ -> retrieve 
# POST: 'authors/' -> create API 
# PUT: 'authors/<int:pk>/ -> update
# PATCH: 'authors/<int:pk>/ -> update / partial_update
# DELETE: 'authors/<int:pk>/ -> destroy API


Another Method to define urls for viewset only defining particular method and urlpattern:
we can bind this viewset into separate views such as:
Eg:

author_list = AuthorViewSet.as_view({'get': 'list'})
author_detail = AuthorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    })

etc.

'''



urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('create/', BookCreateAPIView.as_view(), name='book_create'),
    path('update/<int:pk>', BookUpdateAPIView.as_view(), name='book_update'),
    path('', include(router.urls))
]
