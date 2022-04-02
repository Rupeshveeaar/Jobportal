from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class MyCustomUser(AbstractUser):
    USER_TYPE=(('1','SUPERUSER'),
           ('2','COMPANY'),
           ('3','JOBSEEKER'),
           )
    user_type=models.CharField(choices=USER_TYPE , max_length=80)
    profile_pic=models.ImageField(upload_to='media/')
    verification=models.FileField(upload_to ='media/')




class Company(models.Model):
       company_name=models.OneToOneField(MyCustomUser, on_delete=models.CASCADE)
       company_address=models.TextField()
       contact= models.CharField(max_length=17)
       # job_title=models.CharField(max_length=100)
       # skills= models.CharField(max_length=200)
       # job_description=models.TextField()
       
       
       
       





class Student(models.Model):
       student_name=models.OneToOneField(MyCustomUser, on_delete=models.CASCADE)
       skills = models.CharField(max_length=200)
       experience=models.CharField(max_length=15)
       contact = models.CharField(max_length=17)
       address = models.TextField()



