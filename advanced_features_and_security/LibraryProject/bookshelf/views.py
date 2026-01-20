from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book  
from .forms import BookSearchForm
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)    
def book_list(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.all()
    
    if form.is_valid():
        title = form.cleaned_data['title']
        books = books.filter(title__icontains=title)  # Safe search
    
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

books = books.filter(title__icontains=title)
