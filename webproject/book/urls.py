from django.urls import path
from views.member_views import *
from django.contrib.auth import views as auth_views
app_name = "book"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login')
]