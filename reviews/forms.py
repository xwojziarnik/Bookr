from django import forms
from .models import Publisher, Review, Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class InstanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        if kwargs.get("instance"):
            button_title = "Zapisz"
        else:
            button_title = "Utwórz"

        self.helper.add_input(Submit("", button_title))


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(required=False, choices=(("title", "Title"), ("contributor", "Contributor")))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.add_input(Submit("", "Wyszukaj"))


class PublisherForm(InstanceForm):
    class Meta:
        model = Publisher
        fields = "__all__"


class ReviewForm(InstanceForm):
    class Meta:
        model = Review
        exclude = ["date_edited", "book"]

    rating = forms.IntegerField(min_value=0, max_value=5)


class BookMediaForm(InstanceForm):
    class Meta:
        model = Book
        fields = ["cover", "sample"]
