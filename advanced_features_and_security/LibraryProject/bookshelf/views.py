from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book  # make sure this matches your Book model

# View to list books
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
