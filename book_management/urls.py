from django.urls import path
from .views import BookCreateView, FormSuccessView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('book-record-create/', BookCreateView.as_view(), name="book_create"),
    path('entry-success/', FormSuccessView.as_view(), name="form_success"),
    path('book-record-update/<int:pk>/', BookUpdateView.as_view(), name="book_update"),
    path('book-record-delete/<int:pk>/', BookDeleteView.as_view(), name="book_delete"),
]
