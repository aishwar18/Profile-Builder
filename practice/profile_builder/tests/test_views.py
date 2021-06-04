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
    def test_load_passwordReset(self):
        response = self.client.get(reverse('passwordReset'))
        self.assertEqual(response.status_code, 200)
    def test_load_changePassword(self):
        response = self.client.get(reverse('changePassword'))
        self.assertEqual(response.status_code, 200)
    def test_load_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
    def test_load_home(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_load_teacher_profile(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('teacher_profile',args = [1]))
        self.assertEqual(response.status_code, 200)       
    def test_load_changeMail(self):
        response = self.client.get(reverse('changeMail'))
        self.assertEqual(response.status_code, 200)
    def test_load_editProfile(self):
        response = self.client.get(reverse('editProfile'))
        self.assertEqual(response.status_code, 200)
    def test_load_changeProfilePic(self):
        response = self.client.get(reverse('changeProfilePic'))
    def test_load_myProfile(self):
        response = self.client.get(reverse('myProfile'))
        self.assertEqual(response.status_code, 200)
    def test_load_faculty_detail(self):
        response = self.client.get(reverse('faculty_detail'))
        self.assertEqual(response.status_code, 200)
    def test_load_favourites(self):
        response = self.client.get(reverse('favourites'))
        self.assertEqual(response.status_code, 200)
    def test_load_favouritesView(self):
        response = self.client.get(reverse('favouritesView'))
        self.assertEqual(response.status_code, 200)
    def test_load_favouritesInsert(self):
        response = self.client.get(reverse('favouritesInsert'))
        self.assertEqual(response.status_code, 200)
    def test_load_favouritesDelete(self):
        response = self.client.get(reverse('favouritesDelete'))
        self.assertEqual(response.status_code, 200)
    def test_load_favouritesProject(self):
        response = self.client.get(reverse('favouritesProject'))
        self.assertEqual(response.status_code, 200)
    def test_load_admin(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('admin'))
        self.assertEqual(response.status_code, 200)
    def test_load_adminAreas(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('adminAreas'))
        self.assertEqual(response.status_code, 200)
    def test_load_adminTeachers(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('adminTeachers'))
        self.assertEqual(response.status_code, 200)
    def test_load_adminStudentData(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('adminStudentData'))
        self.assertEqual(response.status_code, 200)
    def test_load_adminTeacherData(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('adminTeacherData'))
        self.assertEqual(response.status_code, 200)
    def test_load_areasDataView(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('areasDataView'))
        self.assertEqual(response.status_code, 200)
    def test_load_areasDataInsert(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('areasDataInsert'))
        self.assertEqual(response.status_code, 200)
    def test_load_areasDataUpdate(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('areasDataUpdate'))
        self.assertEqual(response.status_code, 200)
    def test_load_areasDataUpdateResult(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('areasDataUpdateResult'))
        self.assertEqual(response.status_code, 200)
    def test_load_areasDataDelete(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('areasDataDelete'))
        self.assertEqual(response.status_code, 200)
    def test_load_areasDataDeleteResult(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('areasDataDeleteResult'))
        self.assertEqual(response.status_code, 200)
    def test_load_teachersDataView(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('teachersDataView'))
        self.assertEqual(response.status_code, 200)
    def test_load_teachersDataInsertMain(self):
        response = self.client.get(reverse('teachersDataInsertMain'))
        self.assertEqual(response.status_code, 200)
    def test_load_teachersDataInsert(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('teachersDataInsert'))
        self.assertEqual(response.status_code, 200)
    def test_load_teachersDataUpdate(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('teachersDataUpdate'))
        self.assertEqual(response.status_code, 200)
    def test_load_teachersDataUpdateResult(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('teachersDataUpdateResult'))
        self.assertEqual(response.status_code, 200)
    def test_load_teachersDataDelete(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('teachersDataDelete'))
        self.assertEqual(response.status_code, 200)
    def test_load_teacherDataView(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('teacherDataView'))
        self.assertEqual(response.status_code, 200)
    def test_load_teacherDataDelete(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('teacherDataDelete'))
        self.assertEqual(response.status_code, 200)
    def test_load_studentDataView(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('studentDataView'))
        self.assertEqual(response.status_code, 200)
    def test_load_studentDataDelete(self):
        session = self.client.session
        session['username'] = "aishwarya"
        session.save()
        response = self.client.get(reverse('studentDataDelete'))
        self.assertEqual(response.status_code, 200)