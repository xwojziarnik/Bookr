from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.


class BookCreateView(CreateView):
    model = Book
    fields = ["name", "author"]
    template_name = "book_form.html"
    success_url = "/book-management/entry-success/"


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Rekord modelu Book został zapisany.")


class BookUpdateView(UpdateView):
    model = Book
    fields = ["name", "author"]
    template_name = "book_form.html"
    success_url = "/book-management/entry-success/"


class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_delete_form.html"
    success_url = "/book-management/delete-success/"
