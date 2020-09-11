from django.shortcuts import render,redirect
from django.contrib.auth.models import auth

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
    