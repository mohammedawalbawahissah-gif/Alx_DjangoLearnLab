from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model data.
    Includes validation to prevent future publication years.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Ensure publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model data.
    Includes a nested list of related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
