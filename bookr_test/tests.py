from django.test import TestCase, Client
from .models import Publisher
from django.contrib.auth.models import User

# Create your tests here.


class TestPublisherModel(TestCase):
    def setUp(self):
        self.p = Publisher(name="Packt",
                           website="www.packt.com",
                           email="contact@packt.com")

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)

    def test_str_representation(self):
        self.assertEquals(str(self.p), "Packt")


class TestGreetingView(TestCase):
    """Testowanie widoku powitalnego"""

    def setUp(self):
        self.client = Client()

    def test_greeting_view(self):
        response = self.client.get('/test/greeting/')
        self.assertEquals(response.status_code, 200)


class TestLoggedInGreetingView(TestCase):
    """Testowanie widoku powitalnego dla uwierzytelnionych użytkowników"""

    def setUp(self):
        test_user = User.objects.create_user(username="testuser", password="test123!")
        test_user.save()
        self.client = Client()

    def test_user_greeting_not_authenticated(self):
        response = self.client.get('test/greet-user/')
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        login = self.client.login(username="testuser", password="test123!")
        response = self.client.get('test/greet-user/')
        self.assertEquals(response.status_code, 200)
