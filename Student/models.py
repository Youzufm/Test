from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=20)
    
class Courses(models.Model):
    Course_Name=models.CharField(max_length=50)
    Duaration=models.CharField(max_length=10)
    Fee=models.CharField(max_length=5)

class Payment(models.Model):
    Name=models.CharField(max_length=220)
    Phone=models.CharField(max_length=20)
    Class_Time=models.TimeField()
    Course=models.CharField(max_length=20)
    Date=models.DateField()
    F_Amount=models.CharField(max_length=10)
class Exams(models.Model):
    Name=models.CharField(max_length=220)
    Phone=models.CharField(max_length=10)
    Class_time=models.TimeField()
    Date=models.DateField()
    Hardware=models.CharField(max_length=5)
    Multimedia=models.CharField(max_length=10)
    Webdesign=models.CharField(max_length=5)
    Network=models.CharField(max_length=5)
    Database=models.CharField(max_length=5)
    Programming=models.CharField(max_length=5)
    Thesis_Book=models.CharField(max_length=5)
    Total=models.FloatField()
    Average=models.FloatField()
    Grade=models.CharField(max_length=2)
#---------------------------------------------Teachers Model---------------------------------
class Teachers(models.Model):
    Fullname=models.CharField(max_length=35)
    Phone=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Address=models.CharField(max_length=50)
    Shift=models.CharField(max_length=10)
    Salary=models.FloatField
    #-----------------------------------------Real Students-----------------------------------
class Students(models.Model):
    Fullname=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Course=models.CharField(max_length=100)
    Time=models.TimeField()
    Amount=models.DecimalField(max_digits=5, decimal_places=2)
    Payment_Mode=models.CharField(max_length=5)
    date=models.DateField()
    #---------------------------Create Table Users---------------
class TBusers(models.Model):
    uname=models.CharField(max_length=50)
    uemail=models.CharField(max_length=50)
    upass1=models.CharField(max_length=50)
    upass2=models.CharField(max_length=50)


