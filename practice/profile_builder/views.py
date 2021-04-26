from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
import csv
from .models import Students,State,Teachers,Teachers_data,Teachers_areas_of_interest,projects,favorites
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
            t = Teachers_data.objects.filter(name_of_faculty=name_of_faculty[i])
            id_of_faculty = t[0].id
            teachers_areas_of_interest = Teachers_areas_of_interest(id_of_faculty=id_of_faculty,name_of_faculty=name_of_faculty[i],faculty_research_interest=faculty_research_interest[i])
            teachers_areas_of_interest.save()
    return render(request,"index.html")

def login(request):
    #print("Start!")
    user = None
    if( request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        user = Students.objects.filter(mailid= email, password=password) or Teachers.objects.filter(mailid= email, password=password)
        if (Students.objects.filter(mailid= email, password=password).exists() or Teachers.objects.filter(mailid= email, password=password).exists()):
            request.session['username'] = user[0].username
            #return render(request,"html/home.html", {"username" : user[0].username})
            return redirect('home')
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

        if (Students.objects.filter(username=username).exists() or Teachers.objects.filter(username=username).exists()):
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
        #t = Teachers_data.objects.filter(mail_of_faculty=mailid)
        #id_of_faculty = t[0].id
        if (Students.objects.filter(username=username).exists() or Teachers.objects.filter(username=username).exists()):
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
        print(request.POST)
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
        new_password = request.POST['new password']
        confirm_password = request.POST['confirmPassword']
        if(new_password!=confirm_password):
            messages.info(request,'Confirm password does not match with the new password')
            return render(request,"html/changePassword.html",{'username': username})
        elif (Students.objects.filter(username=username).exists()):
            s = Students.objects.get(username=username)
            s.password = new_password
            s.save()
            print(s)
            messages.info(request,'Password changed successfully')
            return render(request,"html/home.html",{'username':username})
        elif (Teachers.objects.filter(username=username).exists()):
            t = Teachers.objects.get(username=username)
            t.password = new_password
            t.save()
            print(t)
            messages.info(request,'Password changed successfully')
            return render(request,"html/home.html",{'username': username})
        else:
            return render(request,"html/changePassword.html",{'username': username})
    else:
        return render(request,"html/changePassword.html",{'username': username})

def logout(request):
    try:
      del request.session['username']
    except KeyError:
      pass
    return render(request,"html/logout.html")

def home(request):
    username = request.session['username']
    model = Teachers_areas_of_interest
    field_verbose_names=[]
    field_names = ['id_of_faculty','name_of_faculty','faculty_research_interest']
    table_fields = [f for f in model._meta.get_fields() if f.name in  field_names]
    #print(table_fields)
    for f in table_fields:
        if hasattr(f, 'verbose_name'):
            field_verbose_names.append(f.verbose_name)
    data = [[getattr(ins, name) for name in field_names]
            for ins in model.objects.prefetch_related().all()]
    print(data[0])
    return render(request,"html/home.html",{'username': username,'field_names': field_verbose_names, 'data': data})

def teacher_profile(request,id):
    username = request.session['username']
    return render(request,'html/home.html',{'username':username})

def teacher_profile(request,id):
    username = request.session['username']
    teacher = Teachers_data.objects.get(id=id)
    t_aoi = Teachers_areas_of_interest.objects.filter(id_of_faculty=id)
    name = teacher.name_of_faculty
    email =teacher.mail_of_faculty
    location = teacher.location
    department = teacher.department
    position = teacher.position
    bio = teacher.bio_of_faculty
    aoi = []
    for a in t_aoi:
        aoi.append(a.faculty_research_interest)
    return render(request,'html/teacherProfile.html',{'username':username,'name':name, 'id': id, 'bio':bio, 'email':email, 'location': location, 'position':position, 'department':department, 'aoi':aoi})

def changeMail(request):
    username = request.session.get('username')
    if( request.method == 'POST'):
        new_email = request.POST['new email']
        if(Students.objects.filter(mailid=new_email).exists() or Teachers.objects.filter(mailid=new_email).exists()):
            messages.info(request,'Mailid already exists.Use other mail id')
            return render(request,"html/changeMail.html",{'username': username})
        if (Students.objects.filter(username=username).exists()):
            s = Students.objects.get(username=username)
            s.mailid = new_email
            s.save()
            messages.info(request,'Email changed successfully')
            return redirect('home')
        elif (Teachers.objects.filter(username=username).exists()):
            t = Teachers.objects.get(username=username)
            t.mailid = new_email
            t.save()
            messages.info(request,'Email changed successfully')
            return redirect('home')
        else:
            return render(request,"html/changeMail.html",{'username': username})
    else:
        return render(request,"html/changeMail.html",{'username': username})

def editProfile(request):
    username = request.session.get('username')
    return render(request,"html/EditProfile.html",{'username': username})

def changeProfilePic(request):
    username = request.session.get('username')
    user = None
    user = Students.objects.filter(username=username) or Teachers.objects.filter(username=username)
    if(user[0].img==""):
        request.session['profilepic']='..\media\images\change_profile'
    else:
        request.session['profilepic'] = user[0].img.url
    profilepic = request.session.get('profilepic')
    print(profilepic)
    if( request.method == 'POST' and request.FILES['psimg']):
        new_img = request.FILES['psimg']
        if (Students.objects.filter(username=username).exists()):
            s = Students.objects.get(username=username)
            s.img = new_img
            s.save()
            print(new_img)
            messages.info(request,'Profile Picture changed successfully')
            return redirect('home')
        elif (Teachers.objects.filter(username=username).exists()):
            t = Teachers.objects.get(username=username)
            t.img = new_img
            t.save()
            messages.info(request,'Profile Picture changed successfully')
            return redirect('home')
        else:
            return render(request,"html/changeProfilePic.html",{'username': username,'profilepic' : profilepic})
    else:
        return render(request,"html/changeProfilePic.html",{'username': username,'profilepic' : profilepic})

def myProfile(request):
    #profil pic
    username = request.session.get('username')
    user = None
    user = Students.objects.filter(username=username) or Teachers.objects.filter(username=username)
    if(user[0].img==""):
        request.session['profilepic']='..\media\images\change_profile'
    else:
        request.session['profilepic'] = user[0].img.url
    profilepic = request.session.get('profilepic')
    print(profilepic)
    username = request.session.get('username')
    student = Students.objects.filter(username=username)
    teacher =Teachers.objects.filter(username=username)
    is_student = False
    if(student):
        email = student[0].mailid
        first_name = student[0].first_name
        last_name = student[0].last_name
        college = student[0].college
        degree = student[0].degree
        branch = student[0].branch
        city = student[0].city
        img = student[0].img
        is_student =True
        if(request.method=='POST'):
            if 'lname' in request.POST:
                lname = request.POST['lname']
                if(student):
                    s = Students.objects.get(username=username)
                    s.last_name = lname
                    s.save()
                print(lname)
                return redirect('myProfile')
            if 'fname' in request.POST:
                fname =request.POST['fname']
                if(student):
                    s = Students.objects.get(username=username)
                    s.first_name = fname
                    s.save()
                print(fname)
                return redirect('myProfile')
            if 'col' in request.POST:
                college = request.POST['col']
                if(student):
                    s = Students.objects.get(username=username)
                    s.college = college
                    s.save()
                return redirect('myProfile')
            if 'brh' in request.POST:
                branch = request.POST['brh']
                if(student):
                    s = Students.objects.get(username=username)
                    s.branch = branch
                    s.save()
            if 'deg' in request.POST:
                degree = request.POST['deg']
                if(student):
                    s = Students.objects.get(username=username)
                    s.degree = degree
                    s.save()
                return redirect('myProfile')
            if 'stt' in request.POST and 'sc' in request.POST:
                city = request.POST['sc']
                s = Students.objects.get(username=username)
                s.city = city
                s.save()
                return redirect('myProfile')
        return render(request,"html/myProfile.html",{'username': username, 'email':email,'first_name':first_name, 'last_name':last_name,'college':college,'degree':degree,'branch':branch,'city':city,'img':img,'is_student': is_student,'profilepic' : profilepic})
    elif(teacher):
        is_student=False
        email = teacher[0].mailid
        first_name = teacher[0].first_name
        last_name = teacher[0].last_name
        college = teacher[0].college
        city = teacher[0].city
        img = teacher[0].img
        t = Teachers.objects.get(username=username)
        bio=None
        is_listed = False
        faculty = Teachers_data.objects.get(mail_of_faculty=email)
        if(faculty):
            bio = faculty.bio_of_faculty
            is_listed = True
        if(request.method == 'POST'):
            if 'lname' in request.POST:
                lname = request.POST['lname']
                t.last_name = lname
                t.save()
                return redirect('myProfile')
            if 'fname' in request.POST:
                fname =request.POST['fname']
                t.first_name = fname
                t.save()
                print(fname)
                return redirect('myProfile')
            if 'col' in request.POST:
                college = request.POST['col']
                t.college = college
                t.save()
                return redirect('myProfile')
            if 'stt' in request.POST and 'sc' in request.POST:
                city = request.POST['sc']
                t = Teachers.objects.get(username=username)
                t.city = city
                t.save()
                return redirect('myProfile')


        return render(request,"html/myProfile.html",{'username': username, 'email':email,'first_name':first_name, 'last_name':last_name,'college':college,'city':city,'img':img,'is_student': is_student,'profilepic' : profilepic, 'bio':bio, 'listed':is_listed})

def addFavorites(request):
    username = request.session.get('username')
    area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
    areas1 = []
    for i in area_objects:
        aoi1=i.faculty_research_interest
        aoi=aoi1.capitalize()
        if(aoi and aoi!="-" and aoi not in area_objects):
            aoi.strip()
            areas1.append(aoi)
    areas = sorted(areas1)
    return render(request,"html/addFavourites.html",{'username': username,'areas' : areas})

def faculty_detail(request):
    username = request.session.get('username')
    if (request.method=='POST'):
        t = Teachers.objects.get(username=username)
        #print(t.first_name)
        fname = t.first_name
        lname = t.last_name
        email = t.mailid
        name = fname+" "+lname
        loc = request.POST['loc']
        dept = request.POST['dept']
        pos = request.POST['pos']
        bio =request.POST['bio']
        aoi =request.POST['aoi']
        aoi = aoi.split(',')
        teacher = Teachers_data(name_of_faculty=name, bio_of_faculty=bio, mail_of_faculty = email, position=pos, location=loc, department=dept)
        teacher.save()
        for i in aoi:
            teach  = Teachers_data.objects.filter(mail_of_faculty=email)
            id_of_faculty = teach[0].id
            teachers_aoi = Teachers_areas_of_interest(id_of_faculty=id_of_faculty,name_of_faculty=name,faculty_research_interest=i)
            teachers_aoi.save()
        messages.info(request,"Saved!")
    return render(request,"html/faculty_detail.html",{'username': username})
