from models.member_models import *
from django.forms import ModelForm

class Emailform(ModelForm):
    class Meta:
        model = Member
        field = ['email']

class Mileageform(ModelForm):
    class Meta:
        model = Member
        field = ['email', 'mileage']
