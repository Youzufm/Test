from django.contrib import admin

from .models import Student,Payment,Courses,Exams,Teachers,TBusers,CustomUser
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display="firstname","lastname","country"
class PaymentAdmin(admin.ModelAdmin):
    list_displays="Name","Phone","Class_Time","Course","F_Amount"

class Courses(admin.ModelAdmin):
    list_display="Course_Name","Duaration","Fee"
   
    admin.site.register(Student)
    admin.site.register(Payment)
    admin.site.register(Courses)
    admin.site.register(Exams)
    admin.site.register(Teachers)
    admin.site.register(CustomUser)
    admin.site.register(TBusers)
   
   

