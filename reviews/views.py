from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Used name variable to pass an argument into URL to change the text rendered on web page.

    Example:

    Input:
    https://127.0.0.1:8000
    Output:
    Witaj, świecie!

    Input:
    https://127.0.0.1:8000/?name=Wojtek
    Output:
    Witaj, Wojtek!
    """
    name = request.GET.get("name") or "świecie"
    return HttpResponse("Witaj, {}!".format(name))
