from django.test import SimpleTestCase
from django.urls import reverse,resolve
from profile_builder.views import index,login,register,signup_teachers,signup_students,forgotPassword,passwordReset,changePassword,logout,prQuestion,home

class TestUrls(SimpleTestCase):

    def test_index_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEqual(resolve(url).func, index)

    def test_login_resolved(self):
        url = reverse('login')
        print(resolve(url))
        self.assertEqual(resolve(url).func, login)

    def test_register_resolved(self):
        url = reverse('register')
        print(resolve(url))
        self.assertEqual(resolve(url).func, register)

    def test_signup_students_resolved(self):
        url = reverse('signup_students')
        print(resolve(url))
        self.assertEqual(resolve(url).func, signup_students)

    def test_signup_teachers_resolved(self):
        url = reverse('signup_teachers')
        print(resolve(url))
        self.assertEqual(resolve(url).func, signup_teachers)

    def test_forgot_password_resolved(self):
        url = reverse('forgotPassword')
        print(resolve(url))
        self.assertEqual(resolve(url).func, forgotPassword)

    def test_change_password_resolved(self):
        url = reverse('changePassword')
        print(resolve(url))
        self.assertEqual(resolve(url).func, changePassword)

    def test_password_reset_resolved(self):
        url = reverse('passwordReset')
        print(resolve(url))
        self.assertEqual(resolve(url).func, passwordReset)

    def test_home_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_pr_question_resolved(self):
        url = reverse('prQuestion')
        print(resolve(url))
        self.assertEqual(resolve(url).func, prQuestion)

    def test_logout_resolved(self):
        url = reverse('logout')
        print(resolve(url))
        self.assertEqual(resolve(url).func, logout)
