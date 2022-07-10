from django.urls import path
from .views import index, book_list, book_detail

urlpatterns = [
    path('', index, name='index'),
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name="book_detail")
]
