from django.shortcuts import render
from useraccount.models import Account,Admin,StartUp

# Create your views here.
def index(request):
    values = Account.objects.filter(is_admin=True)
    print(values[1:],"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    imp_values = []
    required_val = values[1:]
    for i in required_val:
        imp_values.append(i.admin_set.all()[0])
    return render(request,'index.html',{'values':imp_values})    
    #return render(request,'index.html')