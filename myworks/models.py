from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Portfolio(models.Model):

    title = models.CharField(max_length = 30, verbose_name = 'project name')
    project_url = models.URLField(max_length=100)
    project_repository = models.URLField(max_length=50)
    description = models.TextField(blank=True)
    technology_used = models.CharField(max_length=15,verbose_name ='technology')
    # image = models.FilePathField(path='/img',default='pathfile')
    date_created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

    

