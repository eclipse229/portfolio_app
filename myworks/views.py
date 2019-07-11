from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Portfolio

# Create your views here.

class ProjectList(ListView):
    model = Portfolio
    template_name = 'project_list.html'
    context_object_name = 'project'
    error_message = 'No application at this moment'

class ProjectDetails(DetailView):
    model = Portfolio
    template_name = 'project_details.html'
    context_object_name = 'project'
