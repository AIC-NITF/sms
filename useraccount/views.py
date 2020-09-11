from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import Account

# Create your views here.
def login(request):
    print("hello")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            print(user)
            print('valid username and password')
            auth.login(request,user)
            return redirect("login")
        else:
            print(user)
            print("invalid password or user name")
            return redirect('login')
    else:
        return render(request,'index.html')


def logout(request):
    print('Hey logout')
    auth.logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        full_name = request.POST['fullname']
        email=request.POST['email']
        uname = request.POST['username']
        password = request.POST['password']
        print(full_name,email,uname,password)
        user = Account.objects.create_user(fullname=full_name,email=email,username=uname)
        user.set_password(password)
        user.save()
        return redirect('index')
    return redirect('index')

    