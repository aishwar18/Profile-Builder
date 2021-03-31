from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
import csv
from . models import Students,State,Teachers,Teachers_data,Teachers_areas_of_interest
import pandas as pd
# Create your views here.

user = None

def index(request):
    if(Teachers_data.objects.count()==0):
        df1 = pd.read_csv('./table1.csv')
        nor1 = df1.shape[0]
        name_of_faculty = pd.Series(df1['name_of_faculty'])
        bio_of_faculty = pd.Series(df1['bio_of_faculty'])
        mail_of_faculty = pd.Series(df1['mail_of_faculty'])
        position = pd.Series(df1['position'])
        department = pd.Series(df1['department'])
        location = pd.Series(df1['location'])
        for i in range(nor1):
            teachers_data = Teachers_data(name_of_faculty=name_of_faculty[i],bio_of_faculty=bio_of_faculty[i],mail_of_faculty=mail_of_faculty[i],position=position[i],location=location[i],department=department[i])
            teachers_data.save()
    if(Teachers_areas_of_interest.objects.count()==0):
        df2 = pd.read_csv('./table2.csv')
        nor2 = df2.shape[0]
        name_of_faculty = pd.Series(df2['name_of_faculty'])
        faculty_research_interest = pd.Series(df2['Area of interest'])
        for i in range(nor2):
            teachers_areas_of_interest = Teachers_areas_of_interest(name_of_faculty=name_of_faculty[i],faculty_research_interest=faculty_research_interest[i])
            teachers_areas_of_interest.save()
    return render(request,"index.html")

def login(request):
    #print("Start!")
    user = None
    if( request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        #print(email,password)
        user = Students.objects.filter(mailid= email, password=password) or Teachers.objects.filter(mailid= email, password=password)
        #print(Students.objects.filter(mailid= email, password=password).exists() or Teachers.objects.filter(mailid= email, password=password).exists())
        if (Students.objects.filter(mailid= email, password=password).exists() or Teachers.objects.filter(mailid= email, password=password).exists()):
            request.session['username'] = user[0].username
            return render(request,"html/home.html", {"user" : user[0]})
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
        security_qn = request.POST['sqn']
        security_an = request.POST['securityanswer']

        if Students.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exists..Choose different Username')
            return redirect('signup_students')
        elif Students.objects.filter(mailid=mailid).exists():
            messages.info(request,'Mail id Already Exists..Choose different Mailid')
            return redirect('signup_students')
        else:
            student = Students(img=img,first_name = first_name,last_name = last_name,college = college,degree = degree,branch = branch,semester = semester,city = city,mailid = mailid,username = username,password = password,security_qn = security_qn,security_an = security_an)
            state = State(city=city,state=state)
            student.save()
            if (not State.objects.filter(city=city).exists()):
                state.save()
            messages.info(request,'Successfully registered! Login to continue.')
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
        security_qn = request.POST['sqn']
        security_an = request.POST['securityanswer']

        if Teachers.objects.filter(username=username).exists():
            messages.info(request,'Username Already Exists. Choose different Username')
            return redirect('signup_teachers')
        elif Teachers.objects.filter(mailid=mailid).exists():
            messages.info(request,'Mail id Already Exists. Choose different Mail id')
            return redirect('signup_teachers')
        else:
            teacher = Teachers(img=img,first_name = first_name,last_name = last_name,college = college,city = city,mailid = mailid,username = username,password = password,security_qn = security_qn,security_an = security_an)
            state = State(city=city,state=state)
            teacher.save()
            if (not State.objects.filter(city=city).exists()):
                state.save()
            messages.info(request,'Successfully registered! Login to continue.')
            return render(request,"index.html")
    else:
        return render(request,"html/signup_teachers.html")

def forgotPassword(request):
    if( request.method == 'POST'):
        username = request.POST.get('username')
        ans = request.POST.get('answer')
        if(Students.objects.filter(username=username).exists() or Teachers.objects.filter(username=username).exists()):
            fp_user = Students.objects.filter(username=username) or Teachers.objects.filter(username=username)
            request.session['question'] = fp_user[0].security_qn
            request.session['answer'] = fp_user[0].security_an
            request.session['fp_username'] = fp_user[0].username
            question = fp_user[0].security_qn
            return render(request,"html/forgotPassword.html", {'question': question})
        else:
            messages.info(request,'No such user!')
            return redirect('forgotPassword')
    else:
        return render(request,"html/forgotPassword.html")

def prQuestion(request):
    if(request.method == 'POST'):
        ans = request.POST.get('answer')
        question = request.session.get('question',False)
        answer = request.session.get('answer',False)
        if(question and answer):
            if(ans):
                if answer.lower().strip()==ans.lower().strip():
                    return render(request,"html/passwordReset.html")
                else:
                    messages.info(request,'Incorrect answer!')
                    return render(request,"html/forgotPassword.html", {'question': question})
            return render(request,"html/forgotPassword.html", {'question': question})
        else:
            messages.info(request,'Error retrieving question!')
            return redirect('forgotPassword')

def passwordReset(request):
    if( request.method == 'POST'):
        username = request.session.get('fp_username')
        new_password = request.POST['newPassword']
        confirm_password = request.POST['confirmPassword']
        print(username, new_password, confirm_password)
        if(new_password!=confirm_password):
            messages.info(request,'Confirm password does not match with the new password')
            return redirect('passwordReset')
        elif (Students.objects.filter(username=username).exists()):
            s = Students.objects.get(username=username)
            s.password = new_password
            s.save()
            messages.info(request,'Password changed successfully')
            del request.session['question']
            del request.session['answer']
            del request.session['fp_username']
            return render(request,"index.html")
        elif (Teachers.objects.filter(username=username).exists()):
            t = Teachers.objects.get(username=username)
            t.password = new_password
            t.save()
            messages.info(request,'Password changed successfully')
            del request.session['question']
            del request.session['answer']
            del request.session['fp_username']
            return render(request,"index.html")
        else:
            del request.session['question']
            del request.session['answer']
            del request.session['fp_username']
            return render(request,"html/forgotPassword.html")
    return render(request,"html/passwordReset.html")

def changePassword(request):
    username = request.session.get('username')
    print(username)
    if( request.method == 'POST'):
        username = request.POST['username']
        new_password = request.POST['new password']
        confirm_password = request.POST['confirm password']
        if(new_password!=confirm_password):
            messages.info(request,'Confirm password does not match with the new password')
            return render(request,"html/changePassword.html",{'username': username})
        elif (Students.objects.filter(username=username).exists()):
            s = Students.objects.get(username=username)
            s.password = new_password
            s.save()
            print(s)
            messages.info(request,'Password changed successfully')
            return render(request,"html/home.html")
        elif (Teachers.objects.filter(username=username).exists()):
            t = Teachers.objects.get(username=username)
            t.password = new_password
            t.save()
            print(t)
            messages.info(request,'Password changed successfully')
            return render(request,"html/home.html")
        else:
            return render(request,"html/changePassword.html")
    else:
        return render(request,"html/changePassword.html")

def logout(request):
    try:
      del request.session['username']
    except:
      pass
    return render(request,"html/logout.html")

def home(request):
    return render(request,"html/home.html")
