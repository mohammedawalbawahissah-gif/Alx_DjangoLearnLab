from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend  # correct import
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering