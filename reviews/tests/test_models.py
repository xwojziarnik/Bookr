from reviews.models import Book, Publisher, Contributor
from django.test import TestCase


class TestPublisherModel(TestCase):
    def test_create_publisher(self):
        publisher = Publisher.objects.create(name="Packt", website="www.packt.com", email="contact@packt.com")
        self.assertIsInstance(publisher, Publisher)


class TestBookModel(TestCase):

    def setUp(self):
        self.publisher = Publisher.objects.create(name='Packt', website='www.packt.com', email='contact@packt.com')
        self.contributor = Contributor.objects.create(first_names='Joe', last_names='Duck', email='hey@jduck.com')

    def test_create_book(self):
        book = Book.objects.create(title="TestBook",
                                   publication_date="2020-01-01",
                                   isbn="0000-00-000",
                                   publisher=self.publisher)
        book.contributors.set([self.contributor])
        self.assertIsInstance(book, Book)

class TestContributorModel(TestCase):
    def test_create_contributor(self):
        contributor = Contributor.objects.create(first_names='Joe', last_names='Duck', email='hey@jduck.com')
        self.assertIsInstance(contributor, Contributor)
