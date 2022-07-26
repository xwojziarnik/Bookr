from django.urls import path
from .views import BookRecordFormView, FormSuccessView

urlpatterns = [
    path('new-book-record/', BookRecordFormView.as_view(), name="book_record_form"),
    path('new-book-record/entry-success/', FormSuccessView.as_view(), name="form_success")
]