from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import Users,auth
from . models import Students,State,Teachers
# Create your views here.

def index(request):
    return render(request,"index.html")

def login(request):
    if( request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email= email, password=password)
        if(user is not None):
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect("login")
    else:
        return render(request,"html/login.html")

def register(request):
    return render(request,"html/register.html")

def signup_students(request):
    if(request.method == 'POST'):
        img = request.POST['psimg']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        college = request.POST['col']
        degree = request.POST['deg']
        branch = request.POST['brh']
        semester = request.POST['sem']
        state = request.POST['stt']
        city = request.POST['sc']
        mailid = request.POST['mail_id']
        username = request.POST['username']
        password = request.POST['password']

        if Students.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exists..Choose different Username')
            return redirect('signup_students')
        elif Students.objects.filter(mailid=mailid).exists():
            messages.info(request,'Mail id Already Exists..Choose different Mailid')
            return redirect('signup_students')
        else:
            student = Students(img=img,first_name = first_name,last_name = last_name,college = college,degree = degree,branch = branch,semester = semester,city = city,mailid = mailid,username = username,password = password)
            state = State(city=city,state=state)
            student.save()
            if (not State.objects.filter(city=city).exists()):
                state.save()
            messages.info(request,'Successfully registered..Login to continue..')
            return render(request,"index.html")
    else:
        return render(request,"html/signup_students.html")

def signup_teachers(request):
    if(request.method == 'POST'):
        img = request.POST['ptimg']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        college = request.POST['col']
        state = request.POST['stt']
        city = request.POST['sc']
        mailid = request.POST['mail_id']
        username = request.POST['username']
        password = request.POST['password']

        if Teachers.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exists..Choose different Username')
            return redirect('signup_teachers')
        elif Teachers.objects.filter(mailid=mailid).exists():
            messages.info(request,'Mail id Already Exists..Choose different Mailid')
            return redirect('signup_teachers')
        else:
            teacher = Teachers(img=img,first_name = first_name,last_name = last_name,college = college,city = city,mailid = mailid,username = username,password = password)
            state = State(city=city,state=state)
            teacher.save()
            if (not State.objects.filter(city=city).exists()):
                state.save()
            messages.info(request,'Successfully registered..Login to continue..')
            return render(request,"index.html")
    else:
        return render(request,"html/signup_teachers.html")
