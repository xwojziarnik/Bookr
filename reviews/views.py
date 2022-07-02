from django.shortcuts import render

# Create your views here.


def index(request):
    name = "świecie"
    return render(request, "base.html", {"name": name})


def book_search(request):
    """
    Type argument of search query like:
    https://127.0.0.1:8000/book-search?search=<your argument -> str>

    Your parameter should include space between words.

    Default search argument is a blank space.
    """
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})
