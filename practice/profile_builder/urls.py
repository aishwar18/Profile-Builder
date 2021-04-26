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
    path('html/teacherProfile/<int:id>/',views.teacher_profile,name="teacher_profile"),
    path('html/changeMail',views.changeMail,name="changeMail"),
    path('html/changeProfilePic',views.changeProfilePic,name="changeProfilePic"),
    path('html/editProfile',views.editProfile,name="editProfile"),
    path('html/myProfile',views.myProfile,name="myProfile"),
    path('html/faculty_detail',views.faculty_detail,name="faculty_detail"),
]
