from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Optional: separate list-only view
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs (all CRUD operations)
    path('', include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('books_app.urls')),  # make sure your app URLs are included
]

urlpatterns = [
    path('books_all/', BookListView.as_view(), name='book-list'),
]
