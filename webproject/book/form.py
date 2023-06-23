from book.models import *
from django.forms import ModelForm
from models.book_models import Book


class Emailform(ModelForm):
    class Meta:
        model = Member
        field = ['email']

class Mileageform(ModelForm):
    class Meta:
        model = Member
        field = ['email', 'mileage']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'email']

class Orderform(ModelForm):
    class Meta:
        model = Order
        field = ['isbn', 'email', 'mileage']
