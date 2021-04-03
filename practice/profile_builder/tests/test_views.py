'''from django.test import TestCase

class ViewsTestCase(TestCase):
    def test_load_index(self):
        """
        Check if index page loads properly
        """
        response = self.client.get('https://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_load_login(self):
        response = self.client.get('https://127.0.0.1:8000/login')
        self.assertEqual(response.status_code, 200)

    def test_load_register(self):
        response = self.client.get('https://127.0.0.1:8000/register')
        self.assertEqual(response.status_code, 200)

    def test_load_signup_students(self):
        response = self.client.get('https://127.0.0.1:8000/signup_students')
        self.assertEqual(response.status_code, 200)

    def test_load_signup_teachers(self):
        response = self.client.get('https://127.0.0.1:8000/signup_teachers')
        self.assertEqual(response.status_code, 200)

    def test_load_forgotPassword(self):
        response = self.client.get('https://127.0.0.1:8000/forgotPassword')
        self.assertEqual(response.status_code, 200)

    def test_load_changePassword(self):
        response = self.client.get('https://127.0.0.1:8000/changePassword')
        self.assertEqual(response.status_code, 200)

    def test_load_passwordReset(self):
        response = self.client.get('https://127.0.0.1:8000/passwordReset')
        self.assertEqual(response.status_code, 200)'''
