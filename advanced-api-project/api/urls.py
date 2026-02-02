from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book') 

urlpatterns = [
    # Read
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Write
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
    path('', include(router.urls)),
]