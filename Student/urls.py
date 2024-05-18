from django.urls import path
from .import views

urlpatterns = [
    path('',views.au,name="Auth"),
    path('user_login', views.user_login, name='user_login'),
    # path('logout/', views.user_logout, name='logout'),
    path('Userdash', views.Dashbourd, name="Userdash"),
    #---------------------Registration---------------------------------
    path('Home/',views.Home,name="Home"),
     path('Home/Add/',views.Add,name="Add"),
     path('Home/addrec/',views.addrec, name="addrec"),
     path('Home/deleted/<int:id>/',views.deleted,name="deletedc"),
      path('Home/update/<int:id>/',views.update,name="update"),
       path('Home/updaterec<int:id>/',views.updaterec,name="updaterec"),
       #-------------------------Courses----------------------------------
    path('Course/',views.Course,name="Course"),
    path('Course/Addc/',views.Addc,name="Addc"),
     path('Course/addcrec/',views.addcrec, name="addcrec"),
     path('Course/delete_c/<int:id>/',views.delete_c,name="delete"),
      path('Course/updatec/<int:id>/',views.updatec,name="updatec"),
       path('Course/upcrec/<int:id>/',views.upcrec,name="upcrec"),
       #-------------------------------Payments------------------------------
        path('Payment/',views.Payments,name="Payment"),
        path('Payment/Addpayment',views.Addpayment,name="Addpayment"),
        path('Payment/Addpaymentrec',views.Add_payment_rec,name="Add_payment_rec"),
        path("Payment/delete/<int:id>/", views.delete,name="delete"),
        path('Payment/Update/<int:id>/',views.Update,name="Update"),
        path("Payment/Update/rec/<int:id>",views.Update_red_payment,name="Update_red_payment"),
        #----------------------------Exams--------------------------------------
        path('Exam/',views.Exam,name="Exam"),
        path('Exam/Grade',views.Grade,name="Grade"),
        path('Exam/AddExam',views.AddExam,name="AddExam"),
       path('Exam/AddExamred',views.Examred,name="Examred"),
       path('Exam/Update/<int:id>/',views.Update_Exam,name="Update_Exam"),
       path('Exam/Update/<int:id>/',views.update_exam_and_redirect,name="update_exam_and_redirect"),
       path('Exam/deleted/<int:id>/',views.Del_E,name="Delete"),
       #---------------------------Teachers----------------------------
       path('Teachers/',views.teachers,name="Teachers"),
       path('Teachers/Add',views.Addteacher,name="Addteacher"),
       path('Teachers/Techred',views.Addpaymentrec,name="Addpaymentrec"),
       path('Teachers/Update/<int:id>/',views.Updateteacher,name="Update"),
       path('Teachers/Update/Update_red_teach/<int:id>/',views.Update_red_teach,name="Update_red_teach"),
       path('Teachers/delete/<int:id>/',views.deletet),
       #------------------------Users----------------------------------
       path('Users/',views.FCUsers,name="Users"),
       path('Signup/',views.signup_user,name="Signup"),
        path('Users/add',views.useradd,name="useradd"),
          path('Users/adduser',views.adduser,name="adduser"),
        path('Users/updateuser/',views.updateuser, name="updateuser"),
        path('Users/deluser/<int:id>/',views.deluser, name="deluser"),
       path('au/',views.au,name="signup"),
       path('logout/',views.logout,name="logout"),
       path('Grade/',views.Grade,name='Grade'),
       path('studentview',views.studentview,name="studentview"),
       path('Grade/studentview/<int:id>/',views.studentview,name="studentview"),
       path('admindash/',views.admindash,name="admindash"),
       #-----------------Index Path--------------------
       path('Index/',views.Homepage,name="Index"),
      path('About/',views.About,name="About"),
      path('Contact/',views.Contact,name="Contact"),
     
]
