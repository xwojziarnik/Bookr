from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.


class BookCreateView(CreateView):
    model = Book
    fields = ["name", "author"]
    template_name = "book_form.html"
    success_url = "entry-success/"


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Rekord modelu Book został zapisany.")
