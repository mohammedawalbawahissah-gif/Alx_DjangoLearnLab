from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to display details of a single library
class LibraryDetailView(View):
    template_name = 'relationship_app/library_detail.html'

    def get(self, request, pk):
        library = Library.objects.get(pk=pk)
        books = Book.objects.filter(library=library)
        context = {
            'library': library,
            'books': books,
        }
        return render(request, self.template_name, context)
