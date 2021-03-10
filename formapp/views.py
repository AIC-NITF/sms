from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from .models import Startup_app_form,Enterpreneur_form,upload
from django.contrib import messages


def anantya(request):
    return render(request,'application.html')

def startup_form_app(request):
    down = upload.objects.all()[0]
    return render(request,'startup_application_form.html',{'down':down})

def entrepreneur_form(request):
    return render(request,'entrepreneur_form.html')

def entrepreneurform(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        district = request.POST['district']
        company_name = request.POST['company_name']
        designation = request.POST['designation']
        sector = request.POST['sector']
        date_incorporation = request.POST['date_incorporation']
        location = request.POST['location']
        turnover = request.POST['turnover']
        journey = request.POST['journey']
        achievements = request.POST['achievements']
        awards = request.POST['awards']
        impact = request.POST['impact']
        vision = request.POST['vision']
        nomination = request.POST['nomination']
        
        
        post = Enterpreneur_form.objects.create(name=name,contact=contact,email=email,district=district,company_name=company_name,designation=designation,sector=sector,date_incorporation=date_incorporation,location=location,turnover=turnover,journey=journey,achievements=achievements,awards=awards,impact=impact,vision=vision,nomination=nomination)
        post.save()
        messages.add_message(request, messages.INFO, 'Form submited successfully.')
        return redirect('entrepreneur_form')
    return render(request,'entrepreneur_form.html')

def startupform(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        district = request.POST['district']
        company_name = request.POST['company_name']
        designation = request.POST['designation']
        sector = request.POST['sector']
        date_incorporation = request.POST['date_incorporation']
        problem_solving = request.POST['problem_solving']
        solution = request.POST['solution']
        uniqueness = request.POST['uniqueness']
        advantages = request.POST['advantages']
        operation_stage = request.POST['operation_stage']
        revenue = request.POST['revenue']
        startup_img = request.FILES['startup_img']
        vid_link = request.POST['vid_link']
        pitch_startup = request.POST['pitch_startup']

        if pitch_startup == 'Yes':
            folder_file = request.FILES['folder_file']
            post = Startup_app_form.objects.create(name=name,contact=contact,email=email,district=district,company_name=company_name,designation=designation,sector=sector,date_incorporation=date_incorporation,problem_solving=problem_solving,solution=solution,uniqueness=uniqueness,advantages=advantages,operation_stage=operation_stage,revenue=revenue,startup_img=startup_img,vid_link=vid_link,pitch_startup=pitch_startup,folder_file=folder_file)
            post.save()
            messages.add_message(request, messages.INFO, 'Form submited successfully.')
            return redirect('startup_form_app') 
        else:
            post = Startup_app_form.objects.create(name=name,contact=contact,email=email,district=district,company_name=company_name,designation=designation,sector=sector,date_incorporation=date_incorporation,problem_solving=problem_solving,solution=solution,uniqueness=uniqueness,advantages=advantages,operation_stage=operation_stage,revenue=revenue,startup_img=startup_img,vid_link=vid_link,pitch_startup=pitch_startup)
            post.save()
            messages.add_message(request, messages.INFO, 'Form submited successfully.')
            return redirect('startup_form_app') 
    return render(request,'startup_application_form.html')


def details(request):
    ent_val = Enterpreneur_form.objects.all()
    str_val = Startup_app_form.objects.all()
    ent_len = len(ent_val)
    str_len = len(str_val)
    return render(request,'application_details.html',{'ent_len':ent_len,'str_len':str_len,'ent_val':ent_val,'str_val':str_val})

def eligibility(request):
    return render(request,'eligibility.html')