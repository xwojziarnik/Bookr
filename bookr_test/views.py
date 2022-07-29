from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def greeting_view(request):
    return HttpResponse("Witaj w witrynie Bookr! Jedyne miejsce, w którym możesz tworzyć recenzje książek.")
