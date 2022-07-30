from django.urls import path
from .views import greeting_view, greeting_view_user

urlpatterns = [
    path('test/greeting/', greeting_view, name='greeting_view'),
    path('test/greet-user/', greeting_view_user, name="greeting_view_user")
]
