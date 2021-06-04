from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
import csv
from django.core.files.storage import FileSystemStorage
from .models import Students,State,Teachers,Teachers_data,Teachers_areas_of_interest,projects,favorites,admin_data
import pandas as pd
# Create your views here.

user = None

def index(request):
    if(admin_data.objects.count()==0):
        username = 'admin1'
        mailid = 'adminprofilebuilder@gmail.com'
        password = 'aAqwer1!@'
        admin_data1 = admin_data(username=username,mailid=mailid,password=password)
        admin_data1.save()
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
        if(admin_data.objects.filter(mailid= email, password=password).exists()):
            admin = admin_data.objects.filter(mailid= email, password=password)
            request.session['username'] = admin[0].username
            username =  request.session['username']
            #print(username)
            return redirect('admin')
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
    if(request.method == 'POST' and request.FILES['psimg']):
        img = request.FILES['psimg']
        print("IMAGE",img)
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
    if(request.method == 'POST' and request.FILES['ptimg']):
        img = request.FILES['ptimg']
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
    else:
        return render(request,"html/forgotPassword.html")

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
    return render(request,"html/home.html",{'username': username,'field_names': field_verbose_names, 'data': data})

def teacher_profile(request,id):
    username = request.session['username']
    if(Students.objects.filter(username=username).exists() or Teachers.objects.filter(username=username).exists()):
        user = Students.objects.filter(username=username) or Teachers.objects.filter(username=username)
        if(user):
            user_mail = user[0].mailid
            teacher = Teachers_data.objects.get(id=id)
            t_aoi = Teachers_areas_of_interest.objects.filter(id_of_faculty=id)
            name = teacher.name_of_faculty
            email =teacher.mail_of_faculty
            location = teacher.location
            department = teacher.department
            position = teacher.position
            bio = teacher.bio_of_faculty
            t1 = Teachers.objects.filter(id_of_faculty=id)
            same_user=False
            research = None
            if(t1):
                if(t1[0].username==username):
                    same_user = True
            img = None
            if not(t1 or img==""):
                img=None
            else:
                img = t1[0].img.url
                print(img)
            aoi = []
            for a in t_aoi:
                aoi.append(a.faculty_research_interest)
            if 'e_dept' in request.POST:
                new_dept = request.POST['e_dept']
                teacher.department = new_dept
                teacher.save()
                return redirect('teacher_profile', id=id)
            if 'e_pos' in request.POST:
                new_pos = request.POST['e_pos']
                teacher.position = new_pos
                teacher.save()
                return redirect('teacher_profile', id=id)
            if 'e_bio' in request.POST:
                new_bio = request.POST['e_bio']
                teacher.bio_of_faculty = new_bio
                teacher.save()
                return redirect('teacher_profile', id=id)
            if 'e_loc' in request.POST:
                new_loc = request.POST['e_loc']
                teacher.location = new_loc
                teacher.save()
                return redirect('teacher_profile', id=id)
            if  ('aois' in request.POST and 'research' in request.POST):
                aois = request.POST['aois']
                aois = aois.lower()
                r = request.POST['research']
                if not(projects.objects.filter(research=r).exists()):
                    new = projects(id_of_faculty=teacher.id,areas_of_interests=aois,research=r)
                    new.save()        
            proj = projects.objects.filter(id_of_faculty=teacher.id)
            if(proj):
                research = []
                for p in proj:
                    research.append(p.research)
            return render(request,'html/teacherProfile.html',{'username':username,'name':name, 'id': id, 'bio':bio, 'email':email, 'location': location, 'position':position, 'department':department, 'aoi':aoi, 'img':img, 'same_user': same_user, 'research': research, 'user_mail':user_mail})
        return render(request,'html/home.html',{'username':username})
    else:
        return render(request,'html/home.html',{'username':username})

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
            if(t.id_of_faculty!=0):
                t1 = Teachers_data.objects.get(id=t.id_of_faculty)
                t1.mail_of_faculty = new_email
                t1.save()
            messages.info(request,'Email changed successfully')
            return redirect('home')
        else:
            return render(request,"html/changeMail.html",{'username': username})
    else:
        return render(request,"html/changeMail.html",{'username': username})

def editProfile(request):
    username = request.session.get('username')
    return render(request,"html/editProfile.html",{'username': username})

def changeProfilePic(request):
    username = request.session.get('username')
    user = None
    if(Students.objects.filter(username=username).exists() or Teachers.objects.filter(username=username).exists()):
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
    else:
        return render(request,"html/editProfile.html",{'username': username})

def myProfile(request):
    #profil pic
    username = request.session.get('username')
    user = None
    user = Students.objects.filter(username=username) or Teachers.objects.filter(username=username)
    if(user):
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
        aoi = None
        research = None
        fac_id=None
        is_listed = False
        faculty = Teachers_data.objects.filter(mail_of_faculty=email)
        if(faculty):
            bio = faculty[0].bio_of_faculty
            fac_id = faculty[0].id
            fac_aoi = Teachers_areas_of_interest.objects.filter(id_of_faculty=fac_id)
            aoi = []
            for a in fac_aoi:
                aoi.append(a.faculty_research_interest)
            fac_research = projects.objects.filter(id_of_faculty=fac_id)
            if(fac_research):
                research = []
                for p in fac_research:
                    research.append(p.research)
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
        return render(request,"html/myProfile.html",{'username': username, 'email':email,'first_name':first_name, 'last_name':last_name,'college':college,'city':city,'img':img,'is_student': is_student,'profilepic' : profilepic, 'bio':bio, 'listed':is_listed , 'aoi':aoi, 'research':research,'id_of_faculty': fac_id})
    else:
        return render(request,'html/home.html',{'username':username})
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
        faculty = Teachers_data.objects.get(name_of_faculty=name)
        t1 = Teachers.objects.filter(username=username).update(id_of_faculty=faculty.id)
        for i in aoi:
            teach  = Teachers_data.objects.filter(mail_of_faculty=email)
            id_of_faculty = teach[0].id
            teachers_aoi = Teachers_areas_of_interest(id_of_faculty=id_of_faculty,name_of_faculty=name,faculty_research_interest=i)
            teachers_aoi.save()
        messages.info(request,"Saved Successfully!")
    return render(request,"html/faculty_detail.html",{'username': username})


def favourites(request):
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
    return render(request,"html/favourites.html",{'username': username,'areas' : areas})

def favouritesView(request):
    username = request.session.get('username')
    if(Students.objects.filter(username = username).exists() or Teachers.objects.filter(username = username).exists()):
        st = Students.objects.filter(username = username) or Teachers.objects.filter(username = username)
        st = st[0]
        un_st = st.username
        if (favorites.objects.filter(un_st = un_st).exists()):
            user = favorites.objects.filter(un_st = un_st)
            areas = []
            for i in user:
                area = i.research_interest
                areas.append(area)
            return render(request,"html/favouritesView.html",{'areas' : areas})
        else:
            areas = ['No favourites exist']
            return render(request,"html/favouritesView.html",{'areas' : areas})
    else:
        area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
        areas1 = []
        for i in area_objects:
            aoi1=i.faculty_research_interest
            aoi=aoi1.capitalize()
            if(aoi and aoi!="-" and aoi not in area_objects):
                aoi.strip()
                areas1.append(aoi)
        areas = sorted(areas1)
        return render(request,"html/favourites.html",{'username': username,'areas' : areas})        
    

def favouritesInsert(request):
    if(request.method == 'POST'):
        username = request.session.get('username')
        if(Students.objects.filter(username = username).exists() or Teachers.objects.filter(username = username).exists()):
            st = Students.objects.filter(username = username) or Teachers.objects.filter(username = username)
            st = st[0]
            un_st = st.username
            aoi = request.POST['aoi']
            st_ft = favorites(un_st = un_st,research_interest  = aoi)
            st_ft.save()
            messages.info(request,'New data successfully inserted!')
            return redirect('favourites')
        else:
                area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
                areas1 = []
                for i in area_objects:
                    aoi1=i.faculty_research_interest
                    aoi=aoi1.capitalize()
                    if(aoi and aoi!="-" and aoi not in area_objects):
                        aoi.strip()
                        areas1.append(aoi)
                areas = sorted(areas1)
                return render(request,"html/favourites.html",{'username': username,'areas' : areas})      
    else:
        username = request.session.get('username')
        if(Students.objects.filter(username = username).exists() or Teachers.objects.filter(username = username).exists()):
            st = Students.objects.filter(username = username) or Teachers.objects.filter(username = username)
            st = st[0]
            un_st = st.username
            areas = []
            if (favorites.objects.filter(un_st = un_st).exists()):
                user = favorites.objects.filter(un_st = un_st)
                for i in user:
                    area = i.research_interest
                    areas.append(area)
            area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
            areas1 = []
            for i in area_objects:
                aoi1=i.faculty_research_interest
                aoi=aoi1.lower()
                if(aoi and aoi!="-" and aoi not in area_objects):
                    aoi.strip()
                    if(aoi not in areas):
                        areas1.append(aoi)
            areas = sorted(areas1)
            return render(request,"html/favouritesInsert.html",{'areas' : areas})
        else:
            area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
            areas1 = []
            for i in area_objects:
                aoi1=i.faculty_research_interest
                aoi=aoi1.capitalize()
                if(aoi and aoi!="-" and aoi not in area_objects):
                    aoi.strip()
                    areas1.append(aoi)
            areas = sorted(areas1)
            return render(request,"html/favourites.html",{'username': username,'areas' : areas})      

def favouritesDelete(request):
    if(request.method == 'POST'):
        username = request.session.get('username')
        if(Students.objects.filter(username = username).exists() or Teachers.objects.filter(username = username).exists()):
            st = Students.objects.filter(username = username) or Teachers.objects.filter(username = username)
            st = st[0]
            un_st = st.username
            if (favorites.objects.filter(un_st = un_st).exists()):
                st = favorites.objects.filter(un_st = un_st)
                aoi = request.POST.getlist('aoi')
                for i in aoi:
                    st1 = favorites.objects.filter(research_interest=i)
                    st1.delete()
                messages.info(request,'Data successfully deleted!')
                return redirect('favourites')
        else:
            area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
            areas1 = []
            for i in area_objects:
                aoi1=i.faculty_research_interest
                aoi=aoi1.capitalize()
                if(aoi and aoi!="-" and aoi not in area_objects):
                    aoi.strip()
                    areas1.append(aoi)
            areas = sorted(areas1)
            return render(request,"html/favourites.html",{'username': username,'areas' : areas})      
    else:
        username = request.session.get('username')
        if(Students.objects.filter(username = username).exists() or Teachers.objects.filter(username = username).exists()):
            st = Students.objects.filter(username = username) or Teachers.objects.filter(username = username)
            st = st[0]
            un_st = st.username
            if (favorites.objects.filter(un_st = un_st).exists()):
                user = favorites.objects.filter(un_st = un_st)
                areas = []
                for i in user:
                    area = i.research_interest
                    areas.append(area)
                return render(request,"html/favouritesDelete.html",{'areas' : areas})
            else:
                areas = ['No favourites exist']
                return render(request,"html/favourites.html",{'areas' : areas})
        else:
            area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
            areas1 = []
            for i in area_objects:
                aoi1=i.faculty_research_interest
                aoi=aoi1.capitalize()
                if(aoi and aoi!="-" and aoi not in area_objects):
                    aoi.strip()
                    areas1.append(aoi)
            areas = sorted(areas1)
            return render(request,"html/favourites.html",{'username': username,'areas' : areas})      

def favouritesProject(request):
    username = request.session.get('username')
    if(Students.objects.filter(username = username).exists() or Teachers.objects.filter(username = username).exists()):
        st = Students.objects.filter(username = username) or Teachers.objects.filter(username = username)
        st = st[0]
        un_st = st.username
        if (favorites.objects.filter(un_st = un_st).exists()):
            user = favorites.objects.filter(un_st = un_st)
            pr_fv = []
            areas = []
            for i in user:
                area = i.research_interest
                area = area.strip()
                if(area not in areas):
                    areas.append(area)
                if(projects.objects.filter(areas_of_interests = area).exists()):
                    pr = projects.objects.filter(areas_of_interests = area)
                    l1 = []
                    for i in pr:
                        tid = i.id_of_faculty
                        teacher = Teachers_data.objects.filter(id = tid)
                        tname = teacher[0].name_of_faculty
                        l = [area,tname,i.research]
                        l1.append(l)
                    pr_fv.append(l1)
            if(len(pr_fv)==0):
                area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
                areas1 = []
                for i in area_objects:
                    aoi1=i.faculty_research_interest
                    aoi=aoi1.capitalize()
                    if(aoi and aoi!="-" and aoi not in area_objects):
                        aoi.strip()
                        areas1.append(aoi)
                areas = sorted(areas1)
                messages.info(request,'No projects in your favourite subjects!')
                return render(request,"html/favourites.html",{'username': username,'areas' : areas})
            else:
                return render(request,"html/favouritesProject.html",{'projects' : pr_fv,'areas':areas})
        else:
            area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
            areas1 = []
            for i in area_objects:
                aoi1=i.faculty_research_interest
                aoi=aoi1.capitalize()
                if(aoi and aoi!="-" and aoi not in area_objects):
                    aoi.strip()
                    areas1.append(aoi)
            areas = sorted(areas1)
            messages.info(request,'Please add your favourite subjects!')
            return render(request,"html/favourites.html",{'username': username,'areas' : areas})
    else:
        area_objects = Teachers_areas_of_interest.objects.distinct('faculty_research_interest')
        areas1 = []
        for i in area_objects:
            aoi1=i.faculty_research_interest
            aoi=aoi1.capitalize()
            if(aoi and aoi!="-" and aoi not in area_objects):
                aoi.strip()
                areas1.append(aoi)
        areas = sorted(areas1)
        return render(request,"html/favourites.html",{'username': username,'areas' : areas})     

def admin(request):
    username = request.session['username']
    return render(request,"html/admin.html",{'username': username})

def adminAreas(request):
    username = request.session['username']
    return render(request,"html/adminAreas.html",{'username': username})

def adminTeachers(request):
    username = request.session['username']
    return render(request,"html/adminFacultyDetails.html",{'username': username})

def adminUser(request):
    username = request.session['username']
    return render(request,"html/UserData.html",{'username': username})

def adminStudentData(request):
    username = request.session['username']
    return render(request,"html/adminStudentData.html",{'username': username})

def adminTeacherData(request):
    username = request.session['username']
    return render(request,"html/adminTeacherData.html",{'username': username})

def areasDataView(request):
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        if (Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t = Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty)
            id = t[0].id
            return render(request,"html/areasDataViewResult.html",{'id':id,'name':name_of_faculty,'data':t})
        else:
            return render(request,"html/adminAreas.html")
    else:
        items = Teachers_data.objects.all()
        return render(request,"html/areasDataView.html",{'items':items})

def areasDataInsert(request):
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        faculty_research_interest = request.POST['aoi']
        if (Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t=Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty)
            id_of_faculty = t[0].id_of_faculty
            teachers_aoi = Teachers_areas_of_interest(id_of_faculty = id_of_faculty,name_of_faculty=name_of_faculty,faculty_research_interest = faculty_research_interest)
            teachers_aoi.save()
            messages.info(request,'New data successfully inserted!')
            return redirect('areasDataInsert')
        else:
            return render(request,"html/adminAreas.html")
    else:
        items = Teachers_data.objects.all()
        return render(request,"html/areasDataInsert.html",{'items':items})

def areasDataUpdate(request):
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        if (Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t = Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty)
            return render(request,"html/areasDataUpdateResult.html",{'id':id,'name':name_of_faculty,'data':t})
        else:
            return render(request,"html/adminAreas.html")
    else:
        items = Teachers_data.objects.all()
        return render(request,"html/areasDataUpdate.html",{'items':items})

def areasDataUpdateResult(request):
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        if (Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t = Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty)
            j=0
            aoi = request.POST.getlist('aoi')
            for i in t:
                i.faculty_research_interest = aoi[j]
                i.save()
                j+=1
            messages.info(request,'Data successfully updated!')
            return redirect('areasDataUpdate')
        else:
            return render(request,"html/adminAreas.html")
    else:
        return render(request,"html/adminAreas.html")


def areasDataDelete(request):
    username = request.session['username']
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        if (Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t = Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty)
            return render(request,"html/areasDataDeleteResult.html",{'id':id,'name':name_of_faculty,'data':t})
        else:
            return render(request,"html/adminAreas.html")
    else:
        items = Teachers_data.objects.all()
        return render(request,"html/areasDataDelete.html",{'items':items})

def areasDataDeleteResult(request):
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        if (Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t = Teachers_areas_of_interest.objects.filter(name_of_faculty=name_of_faculty)
            aoi = request.POST.getlist('aoi')
            for i in aoi:
                t1 = Teachers_areas_of_interest.objects.filter(faculty_research_interest=i)
                t1.delete()
            messages.info(request,'Data successfully deleted!')
            return redirect('areasDataDelete')
        else:
            return render(request,"html/adminAreas.html")
    else:
        return render(request,"html/adminAreas.html")


def teachersDataView(request):
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        if (Teachers_data.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t = Teachers_data.objects.filter(name_of_faculty=name_of_faculty)
            id = t[0].id
            t=t[0]
            return render(request,"html/TeachersDataViewResult.html",{'id':id,'name':name_of_faculty,'data':t})
        else:
            return redirect('adminTeachers')
    else:
        items = Teachers_data.objects.all()
        return render(request,"html/TeachersDataView.html",{'items':items})
        
def teachersDataInsertMain(request):
    return render(request,"html/teachersDataInsert.html")

def teachersDataInsert(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        bio = request.POST['bio']
        mailid = request.POST['mail_id']
        position = request.POST['position']
        department = request.POST['department']
        location = request.POST['location']

        if (Teachers_data.objects.filter(name_of_faculty=name).exists()):
            messages.info(request,'Faculty details of the given name already exists')
            return redirect('teachersDataInsert')
        elif (Teachers_data.objects.filter(mail_of_faculty=mailid).exists()):
            messages.info(request,'Faculty details of the given mailid already exists')
            return redirect('teachersDataInsert')
        else:
            teachers_data = Teachers_data(name_of_faculty=name,bio_of_faculty=bio,mail_of_faculty=mailid,position=position,location=location,department=department)
            teachers_data.save()
            messages.info(request,'New data successfully inserted!')
            return redirect('adminTeachers')
    else:
        return render(request,"html/teachersDataInsert.html")


def teachersDataUpdate(request):
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        if (Teachers_data.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t = Teachers_data.objects.filter(name_of_faculty=name_of_faculty)
            t=t[0]
            return render(request,"html/teachersDataUpdateResult.html",{'id':id,'name':name_of_faculty,'entry':t})
        else:
             return redirect('adminTeachers')
    else:
        items = Teachers_data.objects.all()
        return render(request,"html/teachersDataUpdate.html",{'items':items})

def teachersDataUpdateResult(request):
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        if (Teachers_data.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t = Teachers_data.objects.filter(name_of_faculty=name_of_faculty)
            t1=t[0]
            d = request.POST
            for i in d.items():
                if(i[0]=='bio_of_faculty'):
                    t1.bio_of_faculty = i[1]
                elif(i[0]=='mail_of_faculty'):
                    t1.mail_of_faculty = i[1]
                elif(i[0]=='position'):
                    t1.position= i[1]
                elif(i[0]=='department'):
                    t1.department = i[1]
                elif(i[0]=='location'):
                    t1.location = i[1]
            t1.save()
            messages.info(request,'Data successfully updated!')
            return redirect('teachersDataUpdate')
        else:
             return redirect('adminTeachers')
    else:
        username = request.session['username']
        return render(request,"html/adminFacultyDetails.html",{'username': username})

def teachersDataDelete(request):
    if(request.method == 'POST'):
        name_of_faculty = request.POST['teacher_name']
        if (Teachers_data.objects.filter(name_of_faculty=name_of_faculty).exists()):
            t = Teachers_data.objects.filter(name_of_faculty=name_of_faculty)
            t = t[0]
            id_of_faculty = t.id
            taoi = Teachers_areas_of_interest.objects.filter(id_of_faculty=id_of_faculty)
            for i in taoi:
                i.delete()
            t.delete()
            messages.info(request,'Data successfully deleted!')
            items = Teachers_data.objects.all()
            return render(request,"html/teachersDataDelete.html",{'items':items})
        else:
            return redirect('tecahersDataDelete')
    else:
        items = Teachers_data.objects.all()
        return render(request,"html/teachersDataDelete.html",{'items':items})


def teacherDataView(request):
    if(request.method == 'POST'):
        mailid = request.POST['mail_id']
        if (Teachers.objects.filter(mailid = mailid).exists()):
            t = Teachers.objects.filter(mailid = mailid)
            t=t[0]
            return render(request,"html/teacherDataViewResult.html",{'data':t})
        else:
            return redirect('UserData')
    else:
        items = Teachers.objects.all()
        return render(request,"html/teacherDataView.html",{'items':items})   

def teacherDataDelete(request):
    if(request.method == 'POST'):
        mailid = request.POST['mail_id']
        if (Teachers.objects.filter(mailid = mailid).exists()):
            t = Teachers.objects.filter(mailid = mailid)
            t = t[0]
            t.delete()
            messages.info(request,'Data successfully deleted!')
            items = Teachers.objects.all()
            return render(request,"html/teacherDataDelete.html",{'items':items})
        else:
            return redirect('teacherDataDelete')
    else:
        items = Teachers.objects.all()
        return render(request,"html/teacherDataDelete.html",{'items':items})

def studentDataView(request):
    if(request.method == 'POST'):
        mailid = request.POST['mail_id']
        if (Students.objects.filter(mailid = mailid).exists()):
            t = Students.objects.filter(mailid = mailid)
            t=t[0]
            return render(request,"html/studentDataViewResult.html",{'data':t})
        else:
            return redirect('adminUser')
    else:
        items = Students.objects.all()
        return render(request,"html/studentDataView.html",{'items':items}) 

def studentDataDelete(request):
    if(request.method == 'POST'):
        mailid = request.POST['mail_id']
        if (Students.objects.filter(mailid = mailid).exists()):
            t = Students.objects.filter(mailid = mailid)
            t = t[0]
            t.delete()
            messages.info(request,'Data successfully deleted!')
            items = Students.objects.all()
            return render(request,"html/studentDataDelete.html",{'items':items})
        else:
            return redirect('studentDataDelete')
    else:
        items = Students.objects.all()
        return render(request,"html/studentDataDelete.html",{'items':items})
