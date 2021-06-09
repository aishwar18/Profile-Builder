from django.test import TestCase, Client
from django.urls import reverse
from importlib import import_module
from django.core.files.uploadedfile import SimpleUploadedFile
from profile_builder.models import Students, Teachers, Teachers_data, Teachers_areas_of_interest, State

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_project_index_GET(self):
        response =  self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_login_GET(self):
        response =  self.client.get('/html/login')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/login.html')

    def test_project_register_GET(self):
        response =  self.client.get('/html/register')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/register.html')

    def test_project_signup_students_POST(self):
        with open('media/images/pic.jpg', 'rb') as img:
            data={'psimg': img,
            'first_name': 'Krishna',
            'last_name': 'Sharma',
            'col': 'Amrita Vishwa Vidhyapeetham',
            'deg': 'B.tech',
            'brh': 'CSE',
            'sem': '6',
            'stt': 'Tamil Nadu',
            'sc': 'Coimbatore',
            'mail_id': 'krishna@gmail.com',
            'username': 'krishna',
            'password': 'Krishna1234',
            'sqn': 'What is your favorite color?',
            'securityanswer': 'blue'}
            response =  self.client.post('/html/signup_students', data, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_signup_teachers_POST(self):
        with open('media/images/pic.jpg', 'rb') as img:
            data={'ptimg': img,
            'first_name': 'Krishna',
            'last_name': 'Sharma',
            'col': 'Amrita Vishwa Vidhyapeetham',
            'deg': 'B.tech',
            'brh': 'CSE',
            'sem': '6',
            'stt': 'Tamil Nadu',
            'sc': 'Coimbatore',
            'mail_id': 'krishna@gmail.com',
            'username': 'krishna',
            'password': 'Krishna1234',
            'sqn': 'What is your favorite color?',
            'securityanswer': 'blue'}
            response =  self.client.post('/html/signup_teachers', data, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_login_POST(self):
        response =  self.client.post('/html/login', {'email' : 'krishna@gmail.com', 'password': 'Krishna1234'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/login.html')

    def test_project_home_GET(self):
        session = self.client.session
        session['username'] = 'test'
        session.save()
        response =  self.client.get('/html/home')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/home.html')

    def test_forgot_password_POST(self):
        session = self.client.session
        session['fp_user'] = 'krishna'
        session['question'] = 'What is your favorite color?'
        session['answer'] = 'blue'
        session.save()
        response =  self.client.post('/html/forgotPassword', {'username' : 'krishna'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/forgotPassword.html')

    def test_pr_question_POST(self):
        session = self.client.session
        session['question'] = 'What is your favorite color?'
        session['answer'] = 'blue'
        session.save()
        response =  self.client.post('/html/prQuestion', {'answer': 'blue'}, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'html/passwordReset.html')

    def test_change_password_POST(self):
        session = self.client.session
        session['username'] = 'krishna'
        session.save()
        response = self.client.post('/html/changePassword', {'new password':'Abcd1234', 'confirmPassword':'Accc1234'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/changePassword.html')

    def test_logout_GET(self):
        session = self.client.session
        session['username'] = 'krishna'
        session.save()
        response = self.client.get('/html/logout')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/logout.html')

    def test_teacher_profile_GET(self,id=1):
        teach = Teachers.objects.create(img = "pic.jpg",id_of_faculty =1,first_name ="Harry",last_name ="Potter", college = "IIT", city = "Chennai", mailid = "harry@gmail.com", username = "Harr1", password ="Harry123", security_qn ="What is your favourite movie?", security_an ="Harry Potter",id=1)
        teach_data = Teachers_data.objects.create(name_of_faculty = "Harry Potter",bio_of_faculty = "Teacher at Hogwarts", mail_of_faculty = "harry@gmail.com",  position = "Assistant Professor", department = "Science", location = "Chennai",id=1)
        session = self.client.session
        session['username'] = 'Harr1'
        session.save()
        response = self.client.get('/html/teacherProfile/1/', kwargs={'id':1})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/teacherProfile.html')

    def test_change_mail_POST(self):
        session = self.client.session
        session['username'] = 'krishna'
        session.save()
        response = self.client.post('/html/changeMail', {'new email':'krishna@gmail.com'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/changeMail.html')

    def test_edit_profile_GET(self):
        session = self.client.session
        session['username'] = 'krishna'
        session.save()
        response = self.client.get('/html/editProfile')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/editProfile.html')

    def test_change_profile_pic_GET(self):
        teach = Teachers.objects.create(img = "pic.jpg",id_of_faculty =1,first_name ="Harry",last_name ="Potter", college = "IIT", city = "Chennai", mailid = "harry@gmail.com", username = "Harr1", password ="Harry123", security_qn ="What is your favourite movie?", security_an ="Harry Potter",id=1)
        session = self.client.session
        session['username'] = 'Harr1'
        session.save()
        response = self.client.get('/html/changeProfilePic')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/changeProfilePic.html')

    def test_my_profile_GET(self):
        teach = Teachers.objects.create(img = "pic.jpg",id_of_faculty =1,first_name ="Harry",last_name ="Potter", college = "IIT", city = "Chennai", mailid = "harry@gmail.com", username = "Harr1", password ="Harry123", security_qn ="What is your favourite movie?", security_an ="Harry Potter",id=1)
        session = self.client.session
        session['username'] = 'Harr1'
        session.save()
        response = self.client.get('/html/myProfile')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/myProfile.html')

    def test_faculty_details_POST(self):
        teach = Teachers.objects.create(img = "pic.jpg",id_of_faculty =1,first_name ="Harry",last_name ="Potter", college = "IIT", city = "Chennai", mailid = "harry@gmail.com", username = "Harr1", password ="Harry123", security_qn ="What is your favourite movie?", security_an ="Harry Potter",id=1)
        session = self.client.session
        session['username'] = 'Harr1'
        session['loc'] = 'Chennai'
        session['dept'] = 'Science'
        session['pos'] = 'Assistant Professor'
        session['bio'] = 'Teacher at Hogwarts'
        session['aoi'] = 'AI'
        session.save()
        response = self.client.get('/html/myProfile')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/myProfile.html')

    def test_favourites_GET(self):
        session = self.client.session
        session['username'] = 'krishna'
        session.save()
        response = self.client.get('/html/favourites')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/favourites.html')

    def test_favouritesView_GET(self):
        session = self.client.session
        session['username'] = 'krishna'
        session.save()
        response = self.client.get('/html/favouritesView', {'areas' : 'Science'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/favourites.html')

    def test_favouritesInsert_POST(self):
        session = self.client.session
        session['username'] = 'krishna'
        session.save()
        response = self.client.post('/html/favouritesInsert')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/favourites.html')

    def test_admin_GET(self):
        response = self.client.get('/html/admin')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/admin.html')

    def test_admin_GET(self):
        session = self.client.session
        session['username'] = 'admin1'
        session.save()
        response = self.client.get('/html/admin')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/admin.html')

    def test_adminAreas_GET(self):
        session = self.client.session
        session['username'] = 'admin1'
        session.save()
        response = self.client.get('/html/adminAreas')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/adminAreas.html')

    def test_adminTeachers_GET(self):
        session = self.client.session
        session['username'] = 'admin1'
        session.save()
        response = self.client.get('/html/adminTeachers')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/adminFacultyDetails.html')

    def test_adminUser_GET(self):
        session = self.client.session
        session['username'] = 'admin1'
        session.save()
        response = self.client.get('/html/adminUser')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/UserData.html')

    def test_adminStudentData_GET(self):
        session = self.client.session
        session['username'] = 'admin1'
        session.save()
        response = self.client.get('/html/adminStudentData')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/adminStudentData.html')

    def test_adminTeacherData_GET(self):
        session = self.client.session
        session['username'] = 'admin1'
        session.save()
        response = self.client.get('/html/adminTeacherData')
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/adminTeacherData.html')

    def test_areasDataView_Negative_POST(self):
        teach = Teachers_areas_of_interest.objects.create(id_of_faculty=1, name_of_faculty="Harry", faculty_research_interest="Machine Learning")
        response = self.client.post('/html/areasDataView', {'teacher_name':'Krishna','aoi':'Machine Learning'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/adminAreas.html')

    def test_areasDataView_POST(self):
        teach = Teachers_areas_of_interest.objects.create(id_of_faculty=1, name_of_faculty="Harry", faculty_research_interest="Machine Learning")
        response = self.client.post('/html/areasDataView', {'teacher_name':'Harry','aoi':'Machine Learning'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/areasDataViewResult.html')

    def test_areasDataInsert_POST(self):
        response = self.client.post('/html/areasDataInsert', {'teacher_name':'Krishna','aoi':'Machine Learning'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/adminAreas.html')

    def test_areasDataUpdate_POST(self):
        response = self.client.post('/html/areasDataUpdate', {'teacher_name':'Krishna'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/adminAreas.html')

    def test_areasDataUpdateResult_POST(self):
        response = self.client.post('/html/areasDataUpdateResult', {'teacher_name':'Krishna'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/adminAreas.html')

    def test_areasDataDelete_POST(self):
        session = self.client.session
        session['username'] = 'admin1'
        session.save()
        teach = Teachers_areas_of_interest.objects.create(id_of_faculty=1, name_of_faculty="Harry", faculty_research_interest="Machine Learning")
        response = self.client.post('/html/areasDataDelete', {'teacher_name':'Harry'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/areasDataDeleteResult.html')

    def test_teachersDataView_Negative_POST(self):
        session = self.client.session
        session['username'] = 'admin1'
        session.save()
        teach = Teachers.objects.create(img = "pic.jpg",id_of_faculty =1,first_name ="Harry",last_name ="Potter", college = "IIT", city = "Chennai", mailid = "harry@gmail.com", username = "Harr1", password ="Harry123", security_qn ="What is your favourite movie?", security_an ="Harry Potter",id=1)
        response = self.client.post('/html/teacherDataView', {'mail_id':'abcd@gmail.com'})
        self.assertRedirects(response, '/html/adminUser', status_code=302,
        target_status_code=200, fetch_redirect_response=True)

    def test_teachersDataView_POST(self):
        teach= Teachers.objects.create(img = "pic.jpg",id_of_faculty =1,first_name ="Harry",last_name ="Potter", college = "IIT", city = "Chennai", mailid = "harry@gmail.com", username = "Harr1", password ="Harry123", security_qn ="What is your favourite movie?", security_an ="Harry Potter",id=1)
        response = self.client.post('/html/teacherDataView', {'mail_id':'harry@gmail.com'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/teacherDataViewResult.html')

    def test_teachersDataDelete_POST(self):
        teach = Teachers.objects.create(img = "pic.jpg",id_of_faculty =1,first_name ="Harry",last_name ="Potter", college = "IIT", city = "Chennai", mailid = "harry@gmail.com", username = "Harr1", password ="Harry123", security_qn ="What is your favourite movie?", security_an ="Harry Potter",id=1)
        response = self.client.post('/html/teacherDataDelete', {'mail_id':'harry@gmail.com'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/teacherDataDelete.html')

    def test_studentDataView_POST(self):
        student = Students.objects.create(img = "pic.jpg",first_name ="Harry",last_name ="Potter", college = "IIT", degree="B.Tech",branch="CSE",semester=6,city = "Chennai", mailid = "harry@gmail.com", username = "Harr1", password ="Harry123", security_qn ="What is your favourite movie?", security_an ="Harry Potter",id=1)
        response = self.client.post('/html/studentDataView', {'mail_id':'harry@gmail.com'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/studentDataViewResult.html')

    def test_studentDataDelete_POST(self):
        student = Students.objects.create(img = "pic.jpg",first_name ="Harry",last_name ="Potter", college = "IIT", degree="B.Tech",branch="CSE",semester=6,city = "Chennai", mailid = "harry@gmail.com", username = "Harr1", password ="Harry123", security_qn ="What is your favourite movie?", security_an ="Harry Potter",id=1)
        response = self.client.post('/html/studentDataDelete', {'mail_id':'harry@gmail.com'})
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'html/studentDataDelete.html')
