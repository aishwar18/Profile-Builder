from django.conf import settings
from django.conf.urls.static import static
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
    path('html/favourites',views.favourites,name="favourites"),
    path('html/admin',views.admin,name="admin"),
    path('html/adminAreas',views.adminAreas,name="adminAreas"),
    path('html/adminTeachers',views.adminTeachers,name="adminTeachers"),
    path('html/adminUser',views.adminUser,name="adminUser"),
    path('html/areasDataView',views.areasDataView,name="areasDataView"),
    path('html/areasDataInsert',views.areasDataInsert,name="areasDataInsert"),
    path('html/areasDataUpdate',views.areasDataUpdate,name="areasDataUpdate"),
    path('html/areasDataUpdateResult',views.areasDataUpdateResult,name="areasDataUpdateResult"),
    path('html/areasDataDelete',views.areasDataDelete,name="areasDataDelete"),
    path('html/areasDataDeleteResult',views.areasDataDeleteResult,name="areasDataDeleteResult"),
    path('html/teachersDataView',views.teachersDataView,name="teachersDataView"),
    path('html/teachersDataInsert',views.teachersDataInsert,name="teachersDataInsert"),
    path('html/teachersDataInsertMain',views.teachersDataInsertMain,name="teachersDataInsertMain"),
    path('html/teachersDataUpdate',views.teachersDataUpdate,name="teachersDataUpdate"),
    path('html/teachersDataUpdateResult',views.teachersDataUpdateResult,name="teachersDataUpdateResult"),
    path('html/teachersDataDelete',views.teachersDataDelete,name="teachersDataDelete"),   
    path('html/adminTeacherData',views.adminTeacherData,name="adminTeacherData"),   
    path('html/teacherDataView',views.teacherDataView,name="teacherDataView"),
    path('html/teacherDataDelete',views.teacherDataDelete,name="teacherDataDelete"),
    path('html/studentDataView',views.studentDataView,name="studentDataView"),
    path('html/studentDataDelete',views.studentDataDelete,name="studentDataDelete"),
    path('html/adminStudentData',views.adminStudentData,name="adminStudentData"),
    path('html/favouritesView',views.favouritesView,name="favouritesView"),
    path('html/favouritesInsert',views.favouritesInsert,name="favouritesInsert"),
    path('html/favouritesDelete',views.favouritesDelete,name="favouritesDelete"),
    path('html/favouritesProject',views.favouritesProject,name="favouritesProject"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)