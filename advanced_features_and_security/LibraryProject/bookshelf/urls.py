from django.urls import path
from .views import example_form_view

urlpatterns = [
    path('example-form/', example_form_view, name='example_form'),
    path('books/', book_list_view, name='book_list'),
]
