from django.test import TestCase
from profile_builder.models import Students,State,Teachers,Teachers_data,Teachers_areas_of_interest,projects,favorites,admin_data

class State_model_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        State.objects.create(city='Coimbatore', state='Tamilnadu')

    def test_city_label(self):
        state_test = State.objects.get(id=1)
        max_length_city = state_test._meta.get_field('city').max_length
        field_label = state_test._meta.get_field('city').verbose_name
        self.assertTrue(isinstance(state_test, State))
        self.assertEqual(field_label,'city')
        self.assertEqual(max_length_city, 100)

    def test_state_label(self):
        state_test = State.objects.get(id=1)
        max_length_state = state_test._meta.get_field('state').max_length
        field_label = state_test ._meta.get_field('state').verbose_name
        self.assertEqual(field_label,'state')
        self.assertTrue(isinstance(state_test, State))
        self.assertEqual(max_length_state, 100)

class Teachers_model_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Teachers.objects.create(img='',first_name = 'Bhaskar',last_name = 'A',college = 'Amrita Vishwa Vidyapeetham',city = 'Coimbatore',mailid = 'bha@gmail.com',username = 'bha',password = 'b@Ha1234a',security_qn = 'What is your favourite sport',security_an = 'Tennis')

    def test_first_name_label(self):
        teachers_test = Teachers.objects.get(id=1)
        max_length = teachers_test._meta.get_field('first_name').max_length
        field_label = teachers_test ._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label,'first name')
        self.assertEqual(max_length, 100)

    def test_last_name_label(self):
        teachers_test = Teachers.objects.get(id=1)
        max_length = teachers_test._meta.get_field('last_name').max_length
        field_label = teachers_test ._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label,'last name')
        self.assertEqual(max_length, 100)

    def test_college_label(self):
        teachers_test = Teachers.objects.get(id=1)
        max_length = teachers_test._meta.get_field('college').max_length
        field_label = teachers_test ._meta.get_field('college').verbose_name
        self.assertEqual(field_label,'college')
        self.assertEqual(max_length, 100)

    def test_city1_label(self):
        teachers_test = Teachers.objects.get(id=1)
        max_length = teachers_test._meta.get_field('city').max_length
        field_label = teachers_test ._meta.get_field('city').verbose_name
        self.assertEqual(field_label,'city')
        self.assertEqual(max_length, 100)

    def test_mailid_label(self):
        teachers_test = Teachers.objects.get(id=1)
        field_label = teachers_test ._meta.get_field('mailid').verbose_name
        self.assertTrue(isinstance(teachers_test,Teachers))
        self.assertEqual(field_label,'mailid')


    def test_username_label(self):
        teachers_test = Teachers.objects.get(id=1)
        max_length = teachers_test._meta.get_field('username').max_length
        field_label = teachers_test ._meta.get_field('username').verbose_name
        self.assertEqual(field_label,'username')
        self.assertEqual(max_length, 100)

    def test_password_label(self):
        teachers_test = Teachers.objects.get(id=1)
        max_length = teachers_test._meta.get_field('password').max_length
        field_label = teachers_test ._meta.get_field('password').verbose_name
        self.assertEqual(field_label,'password')
        self.assertEqual(max_length, 100)

    def test_security_qn_label(self):
        teachers_test = Teachers.objects.get(id=1)
        max_length = teachers_test._meta.get_field('security_qn').max_length
        field_label = teachers_test ._meta.get_field('security_qn').verbose_name
        self.assertEqual(field_label,'security qn')
        self.assertEqual(max_length, 100)

    def test_security_an_label(self):
        teachers_test = Teachers.objects.get(id=1)
        max_length = teachers_test._meta.get_field('security_an').max_length
        field_label = teachers_test ._meta.get_field('security_an').verbose_name
        self.assertEqual(field_label,'security an')
        self.assertEqual(max_length, 100)

class Students_model_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Students.objects.create(img='',first_name = 'Aishwarya',last_name = 'S R',college = 'Amrita Vishwa Vidyapeetham',degree='B.Tech',branch='CSE',semester='6',city = 'Coimbatore',mailid = 'bha@gmail.com',username = 'aishwarya',password = 'b@Ha1234a',security_qn = 'What is your favourite sport',security_an = 'Tennis')

    def test_first_name_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('first_name').max_length
        field_label = students_test ._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label,'first name')
        self.assertEqual(max_length, 100)

    def test_last_name_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('last_name').max_length
        field_label = students_test ._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label,'last name')
        self.assertEqual(max_length, 100)

    def test_college_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('college').max_length
        field_label = students_test ._meta.get_field('college').verbose_name
        self.assertEqual(field_label,'college')
        self.assertEqual(max_length, 100)

    def test_degree_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('degree').max_length
        field_label = students_test ._meta.get_field('degree').verbose_name
        self.assertEqual(field_label,'degree')
        self.assertEqual(max_length, 100)

    def test_branch_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('branch').max_length
        field_label = students_test ._meta.get_field('branch').verbose_name
        self.assertEqual(field_label,'branch')
        self.assertEqual(max_length, 100)

    def test_semester_label(self):
        students_test = Students.objects.get(id=1)
        field_label = students_test ._meta.get_field('semester').verbose_name
        self.assertEqual(field_label,'semester')

    def test_city1_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('city').max_length
        field_label = students_test ._meta.get_field('city').verbose_name
        self.assertEqual(field_label,'city')
        self.assertEqual(max_length, 100)

    def test_mailid_label(self):
        students_test = Students.objects.get(id=1)
        field_label = students_test ._meta.get_field('mailid').verbose_name
        self.assertTrue(isinstance(students_test,Students))
        self.assertEqual(field_label,'mailid')


    def test_username_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('username').max_length
        field_label = students_test ._meta.get_field('username').verbose_name
        self.assertEqual(field_label,'username')
        self.assertEqual(max_length, 100)

    def test_password_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('password').max_length
        field_label = students_test ._meta.get_field('password').verbose_name
        self.assertEqual(field_label,'password')
        self.assertEqual(max_length, 100)

    def test_security_qn_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('security_qn').max_length
        field_label = students_test ._meta.get_field('security_qn').verbose_name
        self.assertEqual(field_label,'security qn')
        self.assertEqual(max_length, 100)

    def test_security_an_label(self):
        students_test = Students.objects.get(id=1)
        max_length = students_test._meta.get_field('security_an').max_length
        field_label = students_test ._meta.get_field('security_an').verbose_name
        self.assertEqual(field_label,'security an')
        self.assertEqual(max_length, 100)

class Teachers_data_model_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Teachers_data.objects.create(name_of_faculty = 'Anisha Radhakrishnan', bio_of_faculty = 'Ms. Anisha Radhakrishnan joined Amrita School of Engineering, Coimbatore in July 2014. She received her BE degree in Computer Science and Engineering from Annamalai University, and M Tech. degree in Computer Science and Engineering from Karunya University. She currently serves as Assistant Professor in the department of Computer Science and Engineering, Amrita School of Engineering. Her areas of interest include Evolutionary computing, Image processing', mail_of_faculty = 'r_anisha@cb.amrita.edu', position = 'Asst. Professor', department = ' Computer Science Engineering,  School of Engineering', location = 'Coimbatore')

    def test_name_of_faculty(self):
        teachers_data_test = Teachers_data.objects.get(id=1)
        field_label = teachers_data_test._meta.get_field('name_of_faculty').verbose_name
        self.assertTrue(isinstance(teachers_data_test, Teachers_data))
        self.assertEqual(field_label,'Name of faculty')

    def test_bio_of_faculty(self):
        teachers_data_test = Teachers_data.objects.get(id=1)
        field_label = teachers_data_test._meta.get_field('bio_of_faculty').verbose_name
        self.assertTrue(isinstance(teachers_data_test, Teachers_data))
        self.assertEqual(field_label,'Bio of faculty')

    def test_mail_of_faculty(self):
        teachers_data_test = Teachers_data.objects.get(id=1)
        field_label = teachers_data_test._meta.get_field('mail_of_faculty').verbose_name
        self.assertTrue(isinstance(teachers_data_test, Teachers_data))
        self.assertEqual(field_label,'Mail of faculty')

    def test_position(self):
        teachers_data_test = Teachers_data.objects.get(id=1)
        field_label = teachers_data_test._meta.get_field('position').verbose_name
        self.assertTrue(isinstance(teachers_data_test, Teachers_data))
        self.assertEqual(field_label,'Position')

    def test_department(self):
        teachers_data_test = Teachers_data.objects.get(id=1)
        field_label = teachers_data_test._meta.get_field('department').verbose_name
        self.assertTrue(isinstance(teachers_data_test, Teachers_data))
        self.assertEqual(field_label,'Department')

    def test_location(self):
        teachers_data_test = Teachers_data.objects.get(id=1)
        field_label = teachers_data_test._meta.get_field('location').verbose_name
        self.assertTrue(isinstance(teachers_data_test, Teachers_data))
        self.assertEqual(field_label,'Location')

class Teachers_areas_of_interest_model_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Teachers_areas_of_interest.objects.create(id_of_faculty = '11', name_of_faculty = 'Anisha Radhakrishnan', faculty_research_interest = 'Data Structure')

    def test_id_of_faculty(self):
        teachers_areas_of_interest_test = Teachers_areas_of_interest.objects.get(id=1)
        field_label = teachers_areas_of_interest_test._meta.get_field('id_of_faculty').verbose_name
        self.assertTrue(isinstance(teachers_areas_of_interest_test, Teachers_areas_of_interest))
        self.assertEqual(field_label,'ID')

    def test_name_of_faculty(self):
        teachers_areas_of_interest_test = Teachers_areas_of_interest.objects.get(id=1)
        field_label = teachers_areas_of_interest_test._meta.get_field('name_of_faculty').verbose_name
        self.assertTrue(isinstance(teachers_areas_of_interest_test, Teachers_areas_of_interest))
        self.assertEqual(field_label,'Name of faculty')
    
    def test_faculty_research_interest(self):
        teachers_areas_of_interest_test = Teachers_areas_of_interest.objects.get(id=1)
        field_label = teachers_areas_of_interest_test._meta.get_field('faculty_research_interest').verbose_name
        self.assertTrue(isinstance(teachers_areas_of_interest_test, Teachers_areas_of_interest))
        self.assertEqual(field_label,'Faculty research interest')

class projects_model_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        projects.objects.create(id_of_faculty = '11', areas_of_interests = 'data structure', research = 'data structure project')

    def test_id_of_faculty(self):
        projects_test = projects.objects.get(id=1)
        field_label = projects_test._meta.get_field('id_of_faculty').verbose_name
        self.assertTrue(isinstance(projects_test, projects))
        self.assertEqual(field_label,'ID')

    def test_areas_of_interests(self):
        projects_test = projects.objects.get(id=1)
        field_label = projects_test._meta.get_field('areas_of_interests').verbose_name
        self.assertTrue(isinstance(projects_test, projects))
        self.assertEqual(field_label,'aoi')

    def test_research(self):
        projects_test = projects.objects.get(id=1)
        field_label = projects_test._meta.get_field('research').verbose_name
        self.assertTrue(isinstance(projects_test, projects))
        self.assertEqual(field_label,'Research')

class favorites_model_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        favorites.objects.create(un_st = 'anisha', research_interest = 'data structure')

    def test_un_st(self):
        favorites_test = favorites.objects.get(id=1)
        field_label = favorites_test._meta.get_field('un_st').verbose_name
        self.assertTrue(isinstance(favorites_test, favorites))
        self.assertEqual(field_label,'User name')

    def test_research_interest(self):
        favorites_test = favorites.objects.get(id=1)
        field_label = favorites_test._meta.get_field('research_interest').verbose_name
        self.assertTrue(isinstance(favorites_test, favorites))
        self.assertEqual(field_label,'Research interest')

class admin_data_model_test(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        admin_data.objects.create(username = 'admin1', mailid = 'adminprofilebuilder@gmail.com', password = 'aAqwer1!@')

    def test_username(self):
        admin_data_test = admin_data.objects.get(id=1)
        self.assertTrue(isinstance(admin_data_test, admin_data))

    def test_mailid(self):
        admin_data_test = admin_data.objects.get(id=1)
        self.assertTrue(isinstance(admin_data_test, admin_data))

    def test_password(self):
        admin_data_test = admin_data.objects.get(id=1)
        self.assertTrue(isinstance(admin_data_test, admin_data))
        max_length = admin_data_test._meta.get_field('password').max_length
        self.assertEqual(max_length, 100)
    
    
