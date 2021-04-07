from django.shortcuts import render

# Create your views here.
def ideanest(request):
    return render(request,'ideanest.html')


def ideanest_form(request):
    return render(request,'ideanest_iframe.html')