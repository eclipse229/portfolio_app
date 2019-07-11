from django.contrib import admin
from .models import Portfolio

# Register your models here.
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title','project_repository',   'project_url', 'date_created',
    'technology_used',]
    list_filter = ['title','technology_used','project_repository','date_created',]

admin.site.register(Portfolio, PortfolioAdmin)
