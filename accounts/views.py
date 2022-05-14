from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

# Create your views here.
def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def registration_success(request):
    if request.method =='POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('password')
                #messages.info(request,"Username Taken")
                return redirect("register")
            elif User.objects.filter(email = email).exists():
               # messages.info(request,"Email Taken")
                print('email')
                print("Email registered already")
                return redirect("register")
            else:

                user = User.objects.create(first_name = firstname,last_name = lastname,email = email,username = username ,password = password1)
                print('last')
                user.set_password(user.password)
                user.save()
    else:
        return render(request,'registration_success')    
    #return redirect("register")
    return render(request,'Successfull.html')