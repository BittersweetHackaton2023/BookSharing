from book.models import *
from django.forms import ModelForm

class Emailform(ModelForm):
    class Meta:
        model = Member
        field = ['email']

class Mileageform(ModelForm):
    class Meta:
        model = Member
        field = ['email', 'mileage']


class Orderform(ModelForm):
    class Meta:
        model = Order
        field = ['isbn', 'email', 'mileage']