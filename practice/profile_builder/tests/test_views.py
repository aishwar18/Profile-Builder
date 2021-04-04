from django.test import TestCase
from django.urls import reverse
class ViewsTestCase(TestCase):
    def test_load_index(self):
        """
        Check if index page loads properly
        """
        response = self.client.get('https://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)
    def test_load_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    def test_load_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
    def test_load_signup_students(self):
        response = self.client.get(reverse('signup_students'))       
        self.assertEqual(response.status_code, 200)
    def test_load_signup_teachers(self):
        response = self.client.get(reverse('signup_teachers'))    
        self.assertEqual(response.status_code, 200)
    def test_load_forgotPassword(self):
        response = self.client.get(reverse('forgotPassword'))    
        self.assertEqual(response.status_code, 200)
    def test_load_changePassword(self):
        response = self.client.get(reverse('changePassword'))
        self.assertEqual(response.status_code, 200)
    def test_load_passwordReset(self):
        response = self.client.get(reverse('passwordReset'))
        self.assertEqual(response.status_code, 200)