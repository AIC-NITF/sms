from django.shortcuts import render,redirect
from django.contrib.auth.models import auth
from .models import Account,Admin,StartUp

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
        full_name = request.POST['full_name']
        email=request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        print(full_name,email,username,password)
        user = Account.objects.create_user(fullname=full_name,email=email,username=username,is_admin=True)
        user.set_password(password)
        user.save() 

        designation = request.POST['designation']
        employee_id = request.POST['employee_id']
        contact_no = request.POST['contact']
        identity_proof = request.POST['identity']

        admin = Admin.objects.create(account=user,designation=designation,employee_id=employee_id,contact_no=contact_no,identity_proof=identity_proof) 
        admin.save()

        return redirect('index')
    return redirect('index')

    