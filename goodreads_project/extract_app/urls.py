from django.urls import path

from .views import book_list, search_books

urlpatterns = [
    path('', book_list, name='book list'),
    path('search', search_books, name='search list'),
]
