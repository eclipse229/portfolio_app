from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage.html'