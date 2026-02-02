from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")

        # Create sample books
        self.book1 = Book.objects.create(title="Python Basics", author="Author A", price=25.0)
        self.book2 = Book.objects.create(title="Advanced Python", author="Author B", price=40.0)

    # ----------------- CRUD Tests -----------------

    def test_create_book(self):
        data = {"title": "Django REST", "author": "Author C", "price": 30.0}
        response = self.client.post("/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "Django REST")

    def test_get_book_list(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        response = self.client.get(f"/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_update_book(self):
        data = {"title": "Python Basics Updated"}
        response = self.client.patch(f"/books/{self.book1.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Python Basics Updated")

    def test_delete_book(self):
        response = self.client.delete(f"/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ----------------- Authentication & Permission Tests -----------------

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.post("/books/", {"title": "Hack Book", "author": "Hacker", "price": 10})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ----------------- Filtering, Searching, Ordering Tests -----------------

    def test_search_books_by_title(self):
        response = self.client.get("/books/?search=Advanced")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Advanced Python")

    def test_filter_books_by_author(self):
        response = self.client.get("/books/?author=Author A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author A")

    def test_order_books_by_price_ascending(self):
        response = self.client.get("/books/?ordering=price")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["price"], 25.0)
        self.assertEqual(response.data[1]["price"], 40.0)

    def test_order_books_by_price_descending(self):
        response = self.client.get("/books/?ordering=-price")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["price"], 40.0)
        self.assertEqual(response.data[1]["price"], 25.0)
