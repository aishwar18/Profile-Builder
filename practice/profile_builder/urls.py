from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('html/login',views.login,name="login"),
    path('html/register',views.register,name="register"),
    path('html/signup_students',views.signup_students,name="signup_students"),
    path('html/signup_teachers',views.signup_teachers,name="signup_teachers"),
    path('html/forgotPassword',views.forgotPassword,name="forgotPassword"),
    path('html/prQuestion',views.prQuestion,name="prQuestion"),
    path('html/changePassword',views.changePassword,name="changePassword"),
    path('html/passwordReset',views.passwordReset,name="passwordReset"),
    path('html/logout',views.logout,name="logout"),
    path('html/home',views.home,name="home"),
    path('html/teacherProfile',views.teacher_profile,name="teacher_profile"),
]
