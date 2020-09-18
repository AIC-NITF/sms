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


def admin_register(request):
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

def startup_register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email=request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        print(full_name,email,username,password)
        user = Account.objects.create_user(fullname=full_name,email=email,username=username,is_startup=True)
        user.set_password(password)
        user.save() 

        startup_name = request.POST['startup_name']
        legal_entity = request.POST['legal_entity']
        founders_designation = request.POST['founders_designation']
        city = request.POST['city']
        website = request.POST['website']
        sector = request.POST['sector']
        team_members = request.POST['team_members']
        location = request.POST['location']
        contact_no = request.POST['contact']

        startup = StartUp.objects.create(account=user,startup_name=startup_name,legal_entity=legal_entity,founders_designation=founders_designation,city=city,website=website,sector=sector,team_members=team_members,location=location,contact_no=contact_no) 
        startup.save()

        return redirect('index')
    return redirect('index') 