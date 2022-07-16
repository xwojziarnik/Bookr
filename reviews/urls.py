from django.urls import path
from .views import index, book_list, book_detail, book_search, publisher_edit

urlpatterns = [
    path('', index, name='index'),
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name="book_detail"),
    path('book-search/', book_search, name='book_search'),
    path('publishers/<int:pk>/', publisher_edit, name='publisher_edit'),
    path('publishers/new/', publisher_edit, name='publisher_create')
]
