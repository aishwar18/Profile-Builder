from django.test import TestCase
from profile_builder.models import Students,State,Teachers,Teachers_data,Teachers_areas_of_interest

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
