from django.urls import path
from .views import greeting_view

urlpatterns = [
    path('test/greeting/', greeting_view, name='greeting_view')
]