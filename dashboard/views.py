from django.shortcuts import render
from useraccount.models import Account


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