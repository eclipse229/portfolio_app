from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from myworks.models import Portfolio

# Create your tests here.

class PortfolioTest(TestCase):
    ''' This is a test for my protfolio application, it lists out all web app works i have done.
    This test tests' the following
    * The portforlio model
    * The views, both the PrrojectList view and ProjectDetial view
    * The templates used
    * The status code
     '''

    def setUp(self):
        self.project = Portfolio.objects.create(
            title = 'my new app',
            description = 'A description of the project',
            project_url = 'www.projecturl.com',
            
        )

    def test_portfoliomodel(self):
        self.assertEqual(self.project.title, 'my new app')
        self.assertEqual(self.project.description, 'A description of the project')
        self.assertEqual(self.project.project_url, 'www.projecturl.com')

    def test_string_representation(self):
        project = Portfolio(title = 'string representation')
        self.assertEqual(str(project), project.title)


    def test_project_view(self):
        response = self.client.get(reverse('projects')) # This test the url name of the view
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_list.html')
    
    def test_project_details(self):
        response = self.client.get('/projects/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project_details.html')
        self.assertContains(response, 'A description of the project')