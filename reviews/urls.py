from django.urls import path, include
from .views import index, book_list, book_detail, book_search, publisher_edit, review_edit, book_media
from .api_views import BookViewSet, ReviewViewSet, Login
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"reviews", ReviewViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('books/', book_list, name='book_list'),
    path('books/<int:pk>/', book_detail, name="book_detail"),
    path('book-search/', book_search, name='book_search'),
    path('publishers/<int:pk>/', publisher_edit, name='publisher_edit'),
    path('publishers/new/', publisher_edit, name='publisher_create'),
    path('books/<book_pk>/reviews/new/', review_edit, name="review_create"),
    path('books/<book_pk>/reviews/<reviews_pk>/', review_edit, name="review_edit"),
    path('books/<int:pk>/media/', book_media, name="book_media"),
    path("api/", include((router.urls, "api"))),
    path("api/login/", Login.as_view(), name="login"),
]
