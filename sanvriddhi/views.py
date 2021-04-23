from django.shortcuts import render

# Create your views here.
def sanvriddhi(request):
    return render(request,'sanvriddhi.html')

def sanvriddhi_form(request):
    return render(request,'iframe.html')
