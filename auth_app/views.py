from django.shortcuts import render , HttpResponse,redirect
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import*

from django.contrib.auth import authenticate,  login,logout
# Create your views here.


from auth_app.models import*
from django.contrib import messages
class EmailBackend(ModelBackend):
    def authenticate(request, username=None, password=None, **Kwargs):
        UserModel=get_user_model()
        try:
            user=UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:     
          if user.check_password(password):   
            return user
        return None 

            
def login_useres(request):
    if request.method == 'POST':
        # user = EmailUserAuth.authenticate(request, username = request.POST['email'],password=request.POST['password'],)
        user=EmailBackend.authenticate(request, username = request.POST.get('email'),password=request.POST.get('password'))
        if user!=None:
            login(request,user)                                        
            user_type = request.user.user_type
            if user_type == '1':
                 return redirect('superadmin')
            elif user_type == '2':
                return redirect('company')
            elif user_type == '3':
                return redirect('student')
        else:
                messages.error(request,"Email and Password are invalid")
                return redirect('login')
        
    else:
            return render(request, 'login.html')

########Company signup ##############

def Signup_company(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        rpassword=request.POST.get('rpassword')
        user=MyCustomUser(username=username , email=email , password=password , user_type=2)
        if password != rpassword:
                messages.error(request,"Password does not match")
                return redirect('Signup_company')
        user.set_password(password)
        if MyCustomUser.objects.filter(username=username).exists():
           messages.error(request, 'Username Already Exists') 
           return redirect('Signup_company')
        if MyCustomUser.objects.filter(email=email).exists():
           messages.error(request, 'Email Already Exists')
           return redirect('Signup_company')
        user.save()
        com=Company(
                company_name=user,
            )
        com.save()
        return redirect('login')    
    return render(request, 'signup-company.html')  

########student signup ##############


def Signup_student(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        rpassword=request.POST.get('rpassword')
        user=MyCustomUser(username=username , email=email , password=password , user_type=3)
        if password != rpassword:
                messages.error(request,"Password does not match")
                return redirect('Signup_student')
        user.set_password(password)
        if MyCustomUser.objects.filter(username=username).exists():
           messages.error(request, 'Username Already Exists') 
           return redirect('Signup_student')
        if MyCustomUser.objects.filter(email=email).exists():
           messages.error(request, 'Email Already Exists')
           return redirect('Signup_student')
        user.save()
        com=Student(
                student_name=user,
            )
        com.save()
        print(com)
        return redirect('login')    
    return render(request, 'signup-student.html')  


def logout_all(request):
    logout(request)
    return redirect('login')

"""
def Signup_student(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        rpassword=request.POST.get('rpassword')
        user=MyCustomUser(username=username , email=email , password=password , user_type=3)
        if password != rpassword:
                messages.error(request,"Password does not match")
                return redirect('Signup_student')
        user.set_password(password)
        user.save()
        com=Company(
                name=user
            )
        com.save()
        return redirect('login')    
    return render(request, 'signup-student.html')   


# def dosuperAgent(request):
#             user = CustomUser(
#                 first_name = fname,
#                 last_name = lname,
#                 username = username,
#                 email = email,               
#                 user_type = 2,
#                 rank = percentage,
                
                
#             )
#             if password1!=password2:

#                 messages.warning(request, "Password Does not match")
#                 return redirect('registeruser')
            
#             user.set_password(password1)
#             user.save()

            
#             agent = SuperAgent(
#                 admin = user,
#                 # rank = rank,
#                 reference_id = Refrence_ID              
 
#             )
#             agent.save()
#             messages.success(request, user.first_name + "  "+ user.last_name + ' Are Successfully Added !!' )
#             return redirect('registeruser')
#     context = {
#         'code':code,
#         'rank':rank
#     }

#     return render(request, 'register-user.html',context)


# def do_admin_signup(request):
#     username=request.POST.get("username")
#     fname=request.POST.get("fname")
   
#     user=CustomUser.objects.create_user(username=username,email=email,password=password,rank=rank,user_type=1)
#     user.first_name = fname
#     user.last_name = lname
    

#         # if password != rpt_password:
#         #     messages.error(request, "Password does not match Try Again " )
#         #     return render('do_admin_signup')


#     user.save()
#     hod = HOD(
#                 admin = user,  
#                 # rank = rank                      
#             )
#     hod.save()
    
    
#     messages.success(request,"Successfully Created Admin")
#     return HttpResponseRedirect(reverse("login"))
    




# def login_user(request):
#     return render(request, 'login.html')
    
# def login_user(request):
#     if request.method == 'POST':
#         user = EmailUserAuth.authenticate(request, 
#                                         username = request.POST.get('email'),
#                                         password=request.POST.get('password'),)
        
#         if user!=None:
#             print('heloooooooooooo')

        
#     return HttpResponse("ddddddd")


#     # if request.method=='POST':
#     #     user=EmailUserAuth.authenticate(request , username=request.POST.get('email'),password=request.POST.get('password'),)
#     #     if user !=None :
#     #         login(request, user)
#     #         user_type=user.user_type
#     #         if user_type=='1':
#     #             return HttpResponse('kasim Super Admin')
#     #         elif user_type=='2':
#     #             return HttpResponse('kasim company')
#     #         elif user_type=='':
#     #             return HttpResponse('kasim jobseeker')
#     #         else:
#     #             return None #messages.error
#     #     else:
#     #         return HttpResponse('login') 
#     # else:        
#     #  return render(request, 'login.html')
"""
