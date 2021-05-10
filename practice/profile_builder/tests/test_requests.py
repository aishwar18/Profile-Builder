from django.test import TestCase, Client
from django.urls import reverse
from importlib import import_module
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
        data={'psimg': 'img.png',
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
        data={'ptimg': 'img.png',
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
