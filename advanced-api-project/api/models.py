from django.db import models

class Author(models.Model):
    """
    Author model represents a writer who can have multiple books.
    This establishes a one-to-many relationship with the Book model.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book written by an author.
    Each book is linked to one author using a ForeignKey.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title