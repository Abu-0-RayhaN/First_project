from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

def authlogin(request):
    if request.method =='POST':
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request,'Email or password invalid!')
    

    return render(request,'authentication/login.html')
def authregistration(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exist():
                messages.error(request,'user name already exist')
            elif User.objects.filter(email=email).exist():
                messages.error(request,'email already exist')
            
            else:
                user=User.objects.create_user(username=username,password=password,email=email)
                user.save()
                return redirect('profile')

        else:
            messages.error(request,'password and confirm password not matched')
    
    return render(request,'authentication/registration.html')
def forgotpassword(request):
    return render(request,'authentication/forgot.html')
def profile(request):
    return render(request,'miapp/profile.html')
def userlogout(request):
    logout(request)
    messages.success(request,'Successfully logged out.')
    return redirect('login')