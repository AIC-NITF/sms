from django.shortcuts import render
from useraccount.models import Account


# Create your views here.
def admin_dashboard(request):
    accounts = Account.objects.all()
    return render(request,'startup.html',{'accounts':accounts})

def startup_dashboard(request):
    return render(request,'dashboard.html')
        
def admin_form(request):
    return render(request,'admin_form.html')