from django.test import TestCase
from .models import Publisher

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
