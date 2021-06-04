from django.test import SimpleTestCase
from django.urls import reverse,resolve
from profile_builder.views import index,login,register,signup_teachers,signup_students,forgotPassword,passwordReset,changePassword,logout,prQuestion,home,teacher_profile,changeMail,changeProfilePic,editProfile,myProfile,faculty_detail,favourites,admin,favouritesView,favouritesDelete,favouritesInsert,favouritesProject,adminAreas,adminUser,adminTeachers,adminStudentData,adminTeacherData, areasDataView, areasDataInsert,areasDataUpdate,areasDataUpdateResult,areasDataDeleteResult,teachersDataView,teachersDataInsert,teachersDataInsertMain,teachersDataDelete,teachersDataUpdate,teachersDataUpdateResult,teacherDataView,teacherDataDelete,studentDataView,studentDataDelete

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

    def test_teacher_profile_resolved(self):
        url = reverse('teacher_profile', kwargs={'id': 1})
        print(resolve(url))
        self.assertEqual(resolve(url).func, teacher_profile)

    def test_change_mail_resolved(self):
        url = reverse('changeMail')
        print(resolve(url))
        self.assertEqual(resolve(url).func, changeMail)

    def test_change_profile_pic_resolved(self):
        url = reverse('changeProfilePic')
        print(resolve(url))
        self.assertEqual(resolve(url).func, changeProfilePic)

    def test_edit_profile_resolved(self):
        url = reverse('editProfile')
        print(resolve(url))
        self.assertEqual(resolve(url).func,editProfile)

    def test_my_profile_resolved(self):
        url = reverse('myProfile')
        print(resolve(url))
        self.assertEqual(resolve(url).func, myProfile)

    def test_faculty_detail_resolved(self):
        url = reverse('faculty_detail')
        print(resolve(url))
        self.assertEqual(resolve(url).func, faculty_detail)

    def test_favourites_resolved(self):
        url = reverse('favourites')
        print(resolve(url))
        self.assertEqual(resolve(url).func, favourites)

    def test_favouritesView_resolved(self):
        url = reverse('favouritesView')
        print(resolve(url))
        self.assertEqual(resolve(url).func, favouritesView)

    def test_favouritesInsert_resolved(self):
        url = reverse('favouritesInsert')
        print(resolve(url))
        self.assertEqual(resolve(url).func, favouritesInsert)

    def test_favouritesDelete_resolved(self):
        url = reverse('favouritesDelete')
        print(resolve(url))
        self.assertEqual(resolve(url).func, favouritesDelete)

    def test_favouritesProject_resolved(self):
        url = reverse('favouritesProject')
        print(resolve(url))
        self.assertEqual(resolve(url).func, favouritesProject)

    def test_admin_resolved(self):
        url = reverse('admin')
        print(resolve(url))
        self.assertEqual(resolve(url).func, admin)

    def test_adminAreas_resolved(self):
        url = reverse('adminAreas')
        print(resolve(url))
        self.assertEqual(resolve(url).func, adminAreas)

    def test_adminStudentData_resolved(self):
        url = reverse('adminStudentData')
        print(resolve(url))
        self.assertEqual(resolve(url).func, adminStudentData)

    def test_adminTeacherData_resolved(self):
        url = reverse('adminTeacherData')
        print(resolve(url))
        self.assertEqual(resolve(url).func, adminTeacherData)

    def test_adminUser_resolved(self):
        url = reverse('adminUser')
        print(resolve(url))
        self.assertEqual(resolve(url).func, adminUser)

    def test_adminTeachers_resolved(self):
        url = reverse('adminTeachers')
        print(resolve(url))
        self.assertEqual(resolve(url).func, adminTeachers)

    def test_areasDataView_resolved(self):
        url = reverse('areasDataView')
        print(resolve(url))
        self.assertEqual(resolve(url).func, areasDataView)

    def test_areasDataInsert_resolved(self):
        url = reverse('areasDataInsert')
        print(resolve(url))
        self.assertEqual(resolve(url).func, areasDataInsert)

    def test_areasDataUpdate_resolved(self):
        url = reverse('areasDataUpdate')
        print(resolve(url))
        self.assertEqual(resolve(url).func, areasDataUpdate)

    def test_areasDataUpdateResult_resolved(self):
        url = reverse('areasDataUpdateResult')
        print(resolve(url))
        self.assertEqual(resolve(url).func, areasDataUpdateResult)

    def test_areasDataDeleteResult_resolved(self):
        url = reverse('areasDataDeleteResult')
        print(resolve(url))
        self.assertEqual(resolve(url).func, areasDataDeleteResult)

    def test_teachersDataView_resolved(self):
        url = reverse('teachersDataView')
        print(resolve(url))
        self.assertEqual(resolve(url).func, teachersDataView)

    def test_teachersDataInsert_resolved(self):
        url = reverse('teachersDataInsert')
        print(resolve(url))
        self.assertEqual(resolve(url).func, teachersDataInsert)

    def test_teachersDataInsertMain_resolved(self):
        url = reverse('teachersDataInsertMain')
        print(resolve(url))
        self.assertEqual(resolve(url).func, teachersDataInsertMain)

    def test_teachersDataDelete_resolved(self):
        url = reverse('teachersDataDelete')
        print(resolve(url))
        self.assertEqual(resolve(url).func, teachersDataDelete)

    def test_teachersDataUpdate_resolved(self):
        url = reverse('teachersDataUpdate')
        print(resolve(url))
        self.assertEqual(resolve(url).func, teachersDataUpdate)

    def test_teachersDataUpdateResult_resolved(self):
        url = reverse('teachersDataUpdateResult')
        print(resolve(url))
        self.assertEqual(resolve(url).func, teachersDataUpdateResult)

    def test_teacherDataView_resolved(self):
        url = reverse('teacherDataView')
        print(resolve(url))
        self.assertEqual(resolve(url).func, teacherDataView)

    def test_teacherDataDelete_resolved(self):
        url = reverse('teacherDataDelete')
        print(resolve(url))
        self.assertEqual(resolve(url).func, teacherDataDelete)

    def test_studentDataView_resolved(self):
        url = reverse('studentDataView')
        print(resolve(url))
        self.assertEqual(resolve(url).func, studentDataView)

    def test_studentDataDelete_resolved(self):
        url = reverse('studentDataDelete')
        print(resolve(url))
        self.assertEqual(resolve(url).func, studentDataDelete)
