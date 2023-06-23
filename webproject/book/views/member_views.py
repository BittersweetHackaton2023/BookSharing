from django.shortcuts import render
from models.member_models import *
from django.contrib.auth.decorators import login_required


def mymileage(request):
    member = request.user.member
    email = models.EmailField(unique=True)