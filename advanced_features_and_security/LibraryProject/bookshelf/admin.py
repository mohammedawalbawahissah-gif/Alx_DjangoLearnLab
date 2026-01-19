from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Columns to show in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Filters on the right sidebar
    list_filter = ('author', 'publication_year')
    
    # Search bar fields
    search_fields = ('title', 'author')
    
    # Optional: make publication year editable directly in the list view
    list_editable = ('publication_year',)
    
    # Optional: sort by publication year by default
    ordering = ('publication_year',)

# Register the Book model with custom admin settings
admin.site.register(Book, BookAdmin)
