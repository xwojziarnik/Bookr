from django.urls import path
from .views import BookCreateView, FormSuccessView

urlpatterns = [
    path('book-record-create/', BookCreateView.as_view(), name="book_create"),
    path('book-record-create/entry-success/', FormSuccessView.as_view(), name="form_success")
]