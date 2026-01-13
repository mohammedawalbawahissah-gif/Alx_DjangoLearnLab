from django.urls import path
from . import views
from .views import LibraryDetailView, list_books



urlpatterns = [
    path('books/', list_books, name='list_books'),              # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]