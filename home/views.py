from django.shortcuts import render,redirect
from useraccount.models import Account,Admin,StartUp,Query
from django.contrib import messages

# Create your views here.
def index(request):
    values = Account.objects.filter(is_admin=True)
    imp_values = []
    required_val = values[1:]
    for i in required_val:
        imp_values.append(i.admin_set.all()[0])
    return render(request,'index.html',{'values':imp_values})    
    #return render(request,'index.html')

def query_message(request):
    if request.method == 'POST':
        name = request.POST['name']
        about = request.POST['about']
        email = request.POST['email']
        message = request.POST['message']
    
        query = Query.objects.create(name=name,about=about,email=email,message=message)
        messages.add_message(request, messages.INFO, 'Query Submitted.')
        return redirect(index)
    return redirect(index)