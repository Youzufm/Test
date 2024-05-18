from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Students,Courses,Payment,Exams,Teachers,TBusers,CustomUser
from django.contrib import messages
import csv
from django.contrib.auth.decorators import login_required

def Dashbourd(request):
    return render(request,'Dashboard/Dashbours1.html')
#-----------------Exam------------------------------
def Exam(request):
    if 'search' in request.GET:
        E=request.GET['search']
        Ex=Exams.objects.filter(Name__icontains=E)
    else:
     Ex=Exams.objects.all()
    return render(request,'Exam/Examplay.html',{'Ex':Ex})
def Imtixan(request):
    return render(request,'Exam/Test.html')
def Grade(request):
    if 'search' in request.GET:
        Ex=request.GET['search']
        Ex=Exams.objects.filter(Name__icontains=Ex)
    else:
     Ex=Exams.objects.all()
    return render(request,'Student Detail/Grade.html',{'Ex':Ex})
    
def AddExam(request):
    return render(request,'Exam/Add_Exam.html')
def Examred(request):
    name=request.POST['name']
    phone=request.POST['phone']
    classtime=request.POST['classtime']
    date=request.POST["date"]
    hardware=request.POST['hardware']
    multimedia=request.POST['multimedia']
    webdesign=request.POST['webdesign']
    network=request.POST['network']
    database=request.POST['database']
    programming=request.POST['programming']
    thesis_book=request.POST['thesis_book']
    total=request.POST['total']
    average=request.POST['average']
    grade=request.POST['grade']
    exam = Exams(
        Name=name,
        Phone=phone,
        Class_time=classtime,
        Date=date,
        Hardware=hardware,
        Multimedia=multimedia,
        Webdesign=webdesign,
        Network=network,
        Database=database,
        Programming=programming,
        Thesis_Book=thesis_book,
        Total=total,
        Average=average,
        Grade=grade,
    )
    messages.success(request, 'Data saved successfully!')
    exam.save()
    return redirect("Exam")
def Update_Exam(request,id):
    exam=Exams.objects.get(id=id)
    return render(request,'Exam/Update.html',{'exam':exam})
def update_exam_and_redirect(request, exam_id):
    exam = Exams.objects.get(id=exam_id)
    if request.method == 'POST':
        exam.Name = request.POST.get('name')
        exam.Phone = request.POST.get('phone')
        exam.Class_time = request.POST.get('class_time')
        exam.Date = request.POST.get('date')
        exam.Hardware = request.POST.get('hardware')
        exam.Multimedia = request.POST.get('multimedia')
        exam.Webdesign = request.POST.get('webdesign')
        exam.Network = request.POST.get('network')
        exam.Database = request.POST.get('database')
        exam.Programming = request.POST.get('programming')
        exam.Thesis_Book = request.POST.get('thesis_book')
        exam.Total = request.POST.get('total')
        exam.Average = request.POST.get('average')
        exam.Grade = request.POST.get('grade')
        exam.save()

        return redirect('Exam')

def Del_E(request,id):
    request
    Ex=Exams.objects.get(id=id)
    Ex.delete()
    return redirect("Exam")
def Dashbourd(request):
    context = {'user': request.user}
    st_count=Students.objects.all().count()
    c_count=Courses.objects.all().count()
    p_count=Payment.objects.all().count()
    t_count=Teachers.objects.all().count()
    e_count=Exams.objects.all().count()
    return render(request,'Dashboard/Dashbours1.html',{'t_count':t_count,'st_count':st_count,'c_count':c_count,'p_count':p_count,'e_count':e_count,},context)
def Home(request):
    if 'search' in request.GET:
        st=request.GET['search']
        st=Students.objects.filter(Fullname__icontains=st)
    else:
     st=Students.objects.all()
    return render(request,'student/Home.html',{'st':st})
def Add(request):
    return render(request,'student/Add.html')
def addrec(request):
    fullname=request.POST['fname']
    phone=request.POST['phone']
    course=request.POST['course']
    stime=request.POST['stime']
    amount=request.POST['amount']
    payment=request.POST['payment']
    date=request.POST['date']
    
    st=Students(Fullname=fullname,Phone=phone,Course=course,Time=stime,Amount=amount,Payment_Mode=payment,date=date)
    st.save()
    return redirect("Home")

def deleted( request,id):
    request
    st = Students.objects.get(id=id)
    st.delete()
    return redirect("Home")
def update(request,id):
    st=Students.objects.get(id=id)
    return render(request,'student/Update.html',{'st':st})
def updaterec(request,id):
    fullname=request.POST['fname']
    phone=request.POST['phone']
    course=request.POST['course']
    stime=request.POST['stime']
    amount=request.POST['amount']
    payment=request.POST['payment']
    date=request.POST['date']
    st=Students.objects.get(id=id)
    st.Fullname=fullname
    st.Phone=phone
    st.Course=course
    st.Time=stime
    st.Amount=amount
    st.Payment_Mode=payment
    st.date=date
    st.save()
    return redirect("Home")
# Waa functionska Courseska
def Course(request):
    if 'search' in request.GET:
        s=request.GET['search']
        crs=Courses.objects.filter(Course_Name__icontains=s)
    else:
     crs=Courses.objects.all()
    return render(request,'Courses/Course.html',{'crs':crs})
def Addc(request):
    return render(request,'Courses/Add.html')
def addcrec(request):
    x=request.POST['Course_Name']
    y=request.POST['Duaration']
    z=request.POST['Fee']
    st=Courses(Course_Name=x,Duaration=y,Fee=z)
    messages.success(request, 'Data saved successfully!')
    st.save()
    return redirect("Course")
def delete_c(request,id):
    request
    crs=Courses.objects.get(id=id)
    messages.success(request, 'Data deleted successfully!')
    crs.delete()
    return redirect("Course")
def updatec(request,id):
    crs=Courses.objects.get(id=id)
    return render(request,'Courses/Update.html',{'crs':crs})
def upcrec(request,cid):
    crs=Courses.objects.get(id=cid)
   
    crs.Course_Name=request.POST.get['Course_Name']
    crs.Duaration=request.POST.get['Duaration']
    crs.Fee=request.POST.get['Fee']
    messages.success(request, 'Data Updated successfully!')
    crs.save()
    return redirect("Course")
#Kani waa payment functionka
def Payments(request):
    if 'search' in request.GET:
        pay=request.GET['search']
        pay=Payment.objects.filter(Name__icontains=pay)
    else:
     pay=Payment.objects.all()
    return render(request,'Payment/Fee.html',{'pay':pay})
def Addpayment(request):
 return render(request,'Payment/Add.html')
def Add_payment_rec(request):
    A=request.POST['name']
    B=request.POST['phone']
    C=request.POST['Time']
    D=request.POST['course']
    E=request.POST['date']
    F=request.POST['amount']
    pay=Payment(Name=A,Phone=B,Class_Time=C,Course=D,Date=E,F_Amount=F)
    messages.success(request, 'Data saved successfully!')
    pay.save()
    return redirect("Payment")
def delete(request,id):
    request
    pay=Payment.objects.get(id=id)
    messages.success(request, 'Data deleted successfully!')
    pay.delete()
    return redirect("Payment")
def Update(request,id):
    py=Payment.objects.get(id=id)
    return render(request,'Payment/Update.html',{'py':py})

def Update_red_payment(request,id):
    x=request.POST['pname']
    y=request.POST['pphone']
    z=request.POST['ptime']
    a=request.POST['pcourse']
    b=request.POST['pdate']
    c=request.POST['pamount']
    pay=Payment.objects.get(id=id)
    pay.Name=x
    pay.Phone=y
    pay.Class_Time=z
    pay.Course=a
    pay.Date=b
    pay.F_Amount=c
    messages.success(request, 'Data Updated successfully!')
    pay.save()
    return redirect("Payment")
#---------------------------------------Teachers-------------------------------------
def teachers(request):
    if 'search' in request.GET:
        tech=request.GET['search']
        tech=Teachers.objects.filter(Fullname__icontains=tech)
    else:
     tech=Teachers.objects.all()
    return render(request,'Teachers/t_display.html',{'tech':tech})
def Addteacher(request):
    return render(request,'Teachers/Add_tech.html')
def Addpaymentrec(request):
    A=request.POST['name']
    B=request.POST['phone']
    C=request.POST['email']
    D=request.POST['address']
    E=request.POST['shift']
    F=request.POST['salary']
    pay=Teachers(Fullname=A,Phone=B,Email=C,Address=D,Shift=E)
    messages.success(request, 'Data saved successfully!')
    pay.save()
    return redirect("Teachers")
def Updateteacher(request,id):
    tech=Teachers.objects.get(id=id)
    return render(request,'Teachers/Update.html',{'tech':tech})
def Update_red_teach(request,id):
    A=request.POST['FULLNAME']
    B=request.POST['PHONE']
    C=request.POST['EMAIL']
    D=request.POST['ADDRESS']
    E=request.POST['SHIFT']
    F=request.POST['SALARY']
    tech=Teachers.objects.get(id=id)
    tech.Fullname=A
    tech.Phone=B
    tech.Email=C
    tech.Address=D
    tech.Shift=E
    tech.Salary=F
    messages.success(request, 'Data Updated successfully!')
    tech.save()
    return redirect("Teachers")
def deletet(request,id):
    request
    tech=Teachers.objects.get(id=id)
    messages.success(request, 'Data deleted successfully!')
    tech.delete()
    return redirect("Teachers")
def Update_Exam(request,id):
    exam=Exams.objects.get(id=id)
    return render(request,'Exam/Updatee.html',{'exam':exam})
def upcrec(request,id):
    exam=Exams.objects.get(id=id)
    exam.Name=request.POST['name']
    exam.Phone=request.POST['phone']
    exam.Class_time=request.POST['classtime']
    exam.Date = request.POST.get('date')
    exam.Hardware = request.POST.get('hardware')
    exam.Multimedia = request.POST.get('multimedia')
    exam.Webdesign = request.POST.get('webdesign')
    exam.Network = request.POST.get('network')
    exam.Database = request.POST.get('database')
    exam.Programming = request.POST.get('programming')
    exam.Thesis_Book = request.POST.get('thesis_book')
    exam.Total = request.POST.get('total')
    exam.Average = request.POST.get('average')
    exam.Grade = request.POST.get('grade')
    exam.save()
    return redirect("Exam")

def au(request):
    return render(request,'Auth/au.html')
def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
             if user.role == 'admin':
                login(request, user)
                return redirect('admindash')
             elif user.role in ['student', 'teacher']:
                login(request, user)
                return redirect('Index')
        else:
            error_message = 'Username or password is incorrect.'
            return render(request, 'Auth/Au.html', {'error_message': error_message})
    return render(request, 'Auth/Au.html')

def signup_user(request):
    return render(request,'Auth/Reg.html')
def studentview(request,id):
    exam=Exams.objects.get(id=id)
    return render(request,'Student Detail/Student trans.html',{'exam':exam})
def admindash(request):
        st_count=Students.objects.all().count()
        c_count=Courses.objects.all().count()
        p_count=Payment.objects.all().count()
        t_count=Teachers.objects.all().count()
        e_count=Exams.objects.all().count()
        g_count=Exams.objects.all().count()
        u_count=TBusers.objects.all().count()
        return render(request,'Dashboard/dashboard.html',{'t_count':t_count,'st_count':st_count,'c_count':c_count,'p_count':p_count,'e_count':e_count,'g_count':g_count,'u_count':u_count})
def FCUsers(request):
 users=CustomUser.objects.all()
 return render(request,'Users/dis_user.html',{'users':users})   
def useradd(request):
 if request.method == 'POST':
    username = request.POST['username']
    email=request.POST['email']
    password1=request.POST['password']
    password2=request.POST['password1']
    us=CustomUser.objects.create_user(username=username,email=email,password=password1)
    us.save()
    return render(request,'Auth/Au.html')
def logout(request):
    return render(request,'Auth/Au.html')
def adduser(request):
    return render(request,'Auth/Reg.html')
def useraddred(request):
 if request.method == 'POST':
    username = request.POST['username']
    email=request.POST['email']
    password1=request.POST['password']
    password2=request.POST['password1']
    us=CustomUser.objects.create_user(username=username,email=email,password=password1)
    us.save()
    return render(request,'Auth/Au.html')
def deluser(request,id):
    user=CustomUser.objects.get(id=id)
    user.save()
    return redirect('Users')
def updateuser(request):
    return render(request,'Users/Update.html')
#---------------------Index Functions--------------------
def Homepage(request):
    return render(request,'Index/Home.html')
def About(request):
    return render(request,'Index/About.html')
def Contact(request):
    return render(request,'Index/Contact.html')