from django.urls import path

from .views import ProjectList, ProjectDetails

urlpatterns = [
    path('', ProjectList.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetails.as_view(), name='details'),
]