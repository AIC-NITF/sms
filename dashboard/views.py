from django.shortcuts import render,get_object_or_404,redirect
from useraccount.models import Account,Admin,StartUp
from .forms import StartUpForm,EmployeeForm


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

def employee_profile_edit(request,pk):
    print("hello guyss",pk)
    content = get_object_or_404(Admin,pk=pk)
    print(content)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=content)
        print(form) 
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            return redirect(dashboard)
    else:
        form = EmployeeForm(instance=content)
        print(form," form")
        print("abcd")
    return render(request,'startup.html',{'form':form})

# def delete_employee(request):
#     details = get_object_or_404(Admin, pk=pk)
#     details.delete()
#     return redirect('dashboard')