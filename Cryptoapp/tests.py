from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from Cryptoapp.models import Cryptocurrency

class Cryptoapp(TestCase):
    

    def test_home_page(self):
        # Test the home page view
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        

    def test_chart_data(self):
       
        symbol = 'usd'  # Replace with a valid symbol for testing
        response = self.client.get(reverse('get_chart_data', args=[symbol]))
        self.assertEqual(response.status_code, 200)
        
        
       