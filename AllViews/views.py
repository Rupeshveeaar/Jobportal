from multiprocessing import context
from winreg import HKEY_LOCAL_MACHINE
from django.contrib import admin
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from auth_app.models import*
from django.contrib import messages

# Create your views here.
def h(request):
    return render(request, 'home.html')


######################## admin views ############################

def SuperAdmin_Profile(request):
    return render(request, 'admin/admin-dashboard.html')


def Update_Admin(request):
    user=request.user.id
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        try:
            customuser = MyCustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            customuser.profile_pic = profile_pic
            customuser.save()
            messages.success(request, "Your Profile Updated Successfully !!")
            return HttpResponseRedirect(reverse("update_admin_profile"))
        except :
            messages.error(request, "Failed to Update Your Profile")
    return render(request, 'admin/update_admin_profile.html',{'user':user})


######################## company views ############################


def Company_Profile(request):
    return render(request, 'company/company-dashboard.html')

def Update_Company(request):
    cmpny=Company.objects.get(company_name_id = request.user.id)
    address = cmpny.company_address
    contact = cmpny.contact
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        address = request.POST.get('address')
        contact= request.POST.get('contact')
        verification= request.FILES.get('verification')
        try:
            user = MyCustomUser.objects.get(id = request.user.id)
            user.first_name = first_name
            user.profile_pic = profile_pic
            user.verification = verification
            user.save()
            cmpny.company_address = address 
            cmpny.contact = contact
            cmpny.save()
            messages.success(request, "Your Profile Updated Successfully !!")
            return redirect('update_company_profile')
        except :
            messages.error(request, "Failed to Update Your Profile")
    context = {
        'add':address,
        'con':contact,
    }
    return render(request, 'company/update_company_profile.html',context)
  
######################## student views ############################

def Student_Profile(request):
    return render(request, 'student/student-dashboard.html')

def Update_Student(request):
    stud=Student.objects.get(student_name_id = request.user.id)
    address = stud.address
    contact = stud.contact
    experience = stud.experience
    skill = stud.skills
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        contact= request.POST.get('contact')
        skill = request.POST.get('skills') 
        experience = request.POST.get('experience') 
        try:
            user = MyCustomUser.objects.get(id = request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.profile_pic = profile_pic
            user.save()
            stud.address = address 
            stud.contact = contact
            stud.skills = skill
            stud.experience = experience

            stud.save()
            messages.success(request, "Your Profile Updated Successfully !!")
            return redirect('update_student_profile')
        except :
            messages.error(request, "Failed to Update Your Profile")
    context = {
        'add':address,
        'con':contact,
        'skl':skill,
        'exp':experience,
    }  
    return render(request, 'student/update_student_profile.html',context)
  

######################## job view ############################

def add_job(request):
    if request.method == "POST":
        job_title=request.POST.get('job_title')
        skills=request.POST.get('skills')
        experience=request.POST.get('experience')
        job_description=request.POST.get('job_description')
        address=request.POST.get('address')
        jobs = Job(job_title=job_title, skills=skills, experience=experience, job_description=job_description, address=address)
        jobs.save()
        messages.success(request,"Job Posted Successfully....... ")
    return render(request,'company/add_job.html')