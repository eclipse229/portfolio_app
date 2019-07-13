from django.urls import path
from .views import Homepage


#path of the homepage

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
]