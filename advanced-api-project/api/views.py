from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(author__icontains=author)
        return queryset

class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single book by ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook for custom creation logic.
        Ensures validation before saving.
        """
        serializer.is_valid(raise_exception=True)
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook for custom update logic.
        """
        serializer.is_valid(raise_exception=True)
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

