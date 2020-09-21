from django.shortcuts import render,get_object_or_404
from useraccount.models import Account,Admin,StartUp


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