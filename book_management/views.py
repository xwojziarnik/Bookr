from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View
from .forms import BookForm

# Create your views here.


class BookRecordFormView(FormView):
    template_name = "book_form.html"
    form_class = BookForm
    success_url = "entry-success/"


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Rekord modelu Book został zapisany.")
