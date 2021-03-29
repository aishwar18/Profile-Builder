from django.db import models
#from . models import 
# Create your models here.

class Students(models.Model):
    img = models.ImageField(upload_to='pics')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    college =  models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    semester = models.IntegerField()
    city = models.CharField(max_length=100)
    mailid = models.TextField()
    username =  models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    security_qn =  models.CharField(max_length=100,default="question")
    security_an =  models.CharField(max_length=100,default="answer")

class State(models.Model):
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Teachers(models.Model):
    img = models.ImageField(upload_to='pics')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    college =  models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    mailid = models.TextField()
    username =  models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    security_qn =  models.CharField(max_length=100,default="question")
    security_an =  models.CharField(max_length=100,default="answer")

class Teachers_data(models.Model):
    name_of_faculty = models.TextField()
    bio_of_faculty = models.TextField()
    mail_of_faculty = models.TextField()
    position = models.TextField()
    department = models.TextField()
    location = models.TextField()
    
class Teachers_areas_of_interest(models.Model):
    name_of_faculty = models.TextField()
    faculty_research_interest = models.TextField()


