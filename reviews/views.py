from django.shortcuts import render

# Create your views here.


def index(request):
    name = "świecie"
    return render(request, "base.html", {"name": name})
