from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


# Create your models here.

class MyCustomUser(AbstractUser):
    USER_TYPE=(('1','SUPERUSER'),
           ('2','COMPANY'),
           ('3','JOBSEEKER'),
           )
    user_type=models.CharField(choices=USER_TYPE , max_length=80)
    profile_pic=models.ImageField(upload_to='media/')
    verification=models.FileField(upload_to ='media/')



############### comapny #######################

class Company(models.Model):
       company_name=models.OneToOneField(MyCustomUser, on_delete=models.CASCADE)
       company_address=models.TextField()
       contact= models.CharField(max_length=17)
       # job_title=models.CharField(max_length=100)
       # skills= models.CharField(max_length=200)
       # job_description=models.TextField()
       
       
       
       



############### student #######################

class Student(models.Model):
       student_name=models.OneToOneField(MyCustomUser, on_delete=models.CASCADE)
       skills = models.CharField(max_length=200)
       experience=models.CharField(max_length=15)
       contact = models.CharField(max_length=17)
       address = models.TextField()



############### job post #######################

class Job(models.Model):
       job_id = models.IntegerField(primary_key=True)
       job_title = models.CharField(max_length=20)
       skills = models.CharField(max_length=100)
       experience = models.CharField(max_length=20)
       job_description = models.TextField()
       address = models.CharField(max_length=100)
       created_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
              return self.job_title



