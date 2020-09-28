from django.shortcuts import render,get_object_or_404,redirect
from useraccount.models import Account,Admin,StartUp
from .forms import StartUpForm


# Create your views here.
def dashboard(request):
    accounts = Account.objects.all()
    user = request.user
    if user.is_admin:
        return render(request,'startup.html',{'accounts':accounts})
    else:
        return render(request,'dashboard.html')
        
def admin_form(request):
    return render(request,'admin_form.html')

def startup_form(request):
    return render(request,'startup_form.html')

def profile(request,pk):
    details = get_object_or_404(Account, pk=pk)
    val = details.startup_set.all()
    print(val[0])
    return render(request,'profile.html',{'value':val[0]})

def startup_profile_edit(request,pk):
    print("hello guyss",pk)
    content = get_object_or_404(StartUp,pk=pk)
    print(content)
    if request.method == 'POST':
        form = StartUpForm(request.POST,instance=content)
        print(form) 
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            return redirect(dashboard)
    else:
        form = StartUpForm(instance=content)
        print(form," form")
    return render(request,'startup_edit_form.html',{'form':form})

def delete_employee(request):
    if request.method == 'POST':
        getpk = request.POST['foo']
        print(getpk)
        details = get_object_or_404(Admin,pk=int(getpk))
        details.delete()
        return redirect('dashboard')



def edit_emp_form(request):

    if request.method == "POST":
        pk = request.POST['pk_val']
        designation = request.POST['designation']
        email = request.POST['email']
        contact = request.POST['contact']

        account = Admin.objects.get(pk=pk)

        if designation:
            designation = designation
        else:
            designation = ' '
        
        if email:
            email = email
        else:
            email = ' '

        if contact:
            contact = contact
        else:
            contact = ' '

        account.update_admin(email = email,designation = designation,contact_no = contact)
    return redirect('dashboard')
    
#user profile
def userprofile(request,pk):
    details = get_object_or_404(Account,pk=pk)
    print(details)
    if details.is_superadmin:
        return render(request,'user_profile.html',{'value':details})
    elif details.is_admin:
        val = details.admin_set.all()
        print(val)
        return render(request,'user_profile.html',{'value':val[0]})
    else:
        val = details.startup_set.all()
        return render(request,'profile',{'value':val[0]})