from django.urls import path
from .views import Homepage, Authorpage


#path of the homepage views

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path ('about/', Authorpage.as_view(), name='about'),
]