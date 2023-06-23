from book.models import *
from django.forms import ModelForm

class Emailform(ModelForm):
    class Meta:
        model = Member
        fields = ['email']

class Mileageform(ModelForm):
    class Meta:
        model = Member
        fields = ['email', 'mileage']


class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = ['isbn', 'email', 'mileage']