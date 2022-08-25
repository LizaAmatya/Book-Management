from books.api.serializers import AuthorSerializer, BookSerializer
from books.models import Author, Book
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [AllowAny]


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        res = {
            'status': True,
            'data': BookSerializer(queryset, many=True).data,
            'message': 'successfully retrieved'
        }

        return Response(data=res, status=status.HTTP_200_OK)


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            book = serializer.save()

        return Response(data={'status': True, 'data': serializer.data, 'msg': 'Successful'}, status=status.HTTP_201_CREATED)


class BookUpdateAPIView(UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    # can include custom permission classes that you create
    permission_classes = [IsAuthenticated]  

    # can override methods: update

    # overriding permission class Example:
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    
    
    def update(self, request, *args, **kwargs):
        obj = self.get_object()

        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid(raise_exception=True):
            book = serializer.save()

        return Response(data={'status': True, 'data': serializer.data, 'msg': 'Successful'}, status=status.HTTP_201_CREATED)


class AuthorViewSet(ModelViewSet):
    
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]
    
    # can override methods: list, create, update, retrieve, partial_update, destroy 
    
    # overriding permission classes
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    # overriding method Eg:
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        
        res = {
            'status': True,
            'message': "Successfully Deleted",
            'data': None
        }
        
        return Response(res, status=status.HTTP_200_OK)
    
