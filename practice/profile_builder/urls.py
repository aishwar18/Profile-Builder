from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('html/login',views.login,name="login"),
    path('html/register',views.register,name="register"),
    path('html/signup_students',views.signup_students,name="signup_students"),
    path('html/signup_teachers',views.signup_teachers,name="signup_teachers"),
    path('html/forgotPassword',views.forgotpassword,name="forgotpassword"),
]
