from django.contrib import admin
from auth_app.models import*
from django.contrib.auth.models import Group 
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.unregister(Group)
# class UserModel(UserAdmin):
#     list_display = ['username', 'user_type']

class MyCustomUserAdmin(admin.ModelAdmin):
    list_display=( 'username','user_type' ,)
admin.site.register(MyCustomUser ,MyCustomUserAdmin )

class StudentUserAdmin(admin.ModelAdmin):
    list_display=( 'student_name' ,)
admin.site.register(Student ,StudentUserAdmin )

class CompanyUserAdmin(admin.ModelAdmin):
    list_display=('company_name' ,)
admin.site.register(Company ,CompanyUserAdmin )
