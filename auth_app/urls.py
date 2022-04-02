from django.contrib import admin
from django.urls import path
from auth_app.views import*
from AllViews.views import*
urlpatterns = [
    path('login' , login_useres , name='login'),
    path('logout' ,logout_all , name='logout'),
    path('' , h , name='h'),
    
############ Admin #########################
    path('superadmin' , SuperAdmin_Profile , name='superadmin'),
    path('update_admin_profile' , Update_Admin , name='update_admin_profile'),

############ Company #########################
    path('signup_company' , Signup_company , name='Signup_company'),
    path('compay' , Company_Profile , name='company'),
    path('update_company_profile' , Update_Company , name='update_company_profile'),

############ Student #########################
    path('signup_student' , Signup_student , name='Signup_student'),
    path('student' , Student_Profile , name='student'),
    path('update_student_profile' , Update_Student , name='update_student_profile'),


]