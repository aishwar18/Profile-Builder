from django.db import models
#from . models import
# Create your models here.

class Students(models.Model):
    img = models.ImageField(upload_to='images/',default='images/view.jpg')
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
    img = models.ImageField(upload_to='images/',default='images/view.jpg')
    id_of_faculty = models.IntegerField(verbose_name = "ID",default=0)
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
    name_of_faculty = models.TextField(verbose_name = "Name of faculty")
    bio_of_faculty = models.TextField(verbose_name = "Bio of faculty")
    mail_of_faculty = models.TextField(verbose_name = "Mail of faculty")
    position = models.TextField(verbose_name = "Position")
    department = models.TextField(verbose_name = "Department")
    location = models.TextField(verbose_name = "Location")

class Teachers_areas_of_interest(models.Model):
    id_of_faculty = models.IntegerField(verbose_name = "ID",default=0)
    name_of_faculty = models.TextField(verbose_name = "Name of faculty")
    faculty_research_interest = models.TextField(verbose_name = "Faculty research interest")

class projects(models.Model):
    id_of_faculty = models.IntegerField(verbose_name = "ID",default=0)
    areas_of_interests = models.TextField(verbose_name = "aoi",default="computer science")
    research = models.TextField(verbose_name = "Research")

class favorites(models.Model):
    un_st =  models.TextField(verbose_name = "User name",default="un")
    research_interest = models.TextField(verbose_name = "Research interest",default="cs")

class admin_data(models.Model):
    username = models.TextField(default="admin1")
    mailid = models.TextField()
    password =  models.CharField(max_length=100)
