from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import auth
import random
from django.core.mail import send_mail
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse,Http404,JsonResponse
from useraccount.models import Session,Sanvriddhi,Account,Submission,Viewer
from .forms import SanvriddhiEditForm

# Create your views here.
def sanvriddhi(request):
    return render(request,'sanvriddhi.html')

def sanvriddhi_form(request):
    return render(request,'iframe.html')


def sanvriddhi_nomination(request):
    return render(request,'sanvriddhi_nomination.html')

def sanvriddhi_dashboard(request):
    if request.user.is_adminstrator or request.user.is_sanvriddhi or request.user.is_viewer:
        sessions = Session.objects.all()
        if request.user.is_adminstrator or request.user.is_viewer:
            participaints = Account.objects.filter(is_sanvriddhi=True)
            lis = []
            for participaint in participaints:
                lis.append(participaint.sanvriddhi_set.all()[0])
            return render(request,'sanvriddhi_dashboard.html',{'sessions':sessions,'participaints':lis})
        else:
            account = request.user
            sanvriddhi_account = account.sanvriddhi_set.all()[0]

            attachements = sanvriddhi_account.submission_set.all()
            return render(request,'sanvriddhi_dashboard.html',{'sessions':sessions,'attachements':attachements,'sanvriddhi_account':sanvriddhi_account})
    else:
        return render(request,'error.html')

def create_session(request):
    if request.method == 'POST':
        session_name = request.POST['session_name']
        session_details = request.POST['session_details']
        session_date = request.POST['session_date']
        time = request.POST['time']
        time_out = request.POST['time_out']
        pm_am1 = request.POST['pm_am1']
        pm_am2 = request.POST['pm_am2']
        meeting_link = request.POST['meeting_link']
        submission_link = request.POST['submission_link']
        if len(request.FILES) != 0:
            pre_read = request.FILES['pre_read']
        else:
            pre_read = None


        session_obj = Session.objects.create(session_name=session_name,session_details=session_details,session_date=session_date,time=time,time_out=time_out,pm_am1=pm_am1,pm_am2=pm_am2,meeting_link=meeting_link,pre_read=pre_read,submission_link=submission_link)
        messages.add_message(request, messages.INFO, 'Session Created Successfully')
        return redirect(sanvriddhi_dashboard)

def submission(request):
    user = request.user
    sanvriddhi_user = user.sanvriddhi_set.all()[0]
    if request.method == 'POST':
        session_topic = request.POST['session_topic']
        if len(request.FILES) != 0:
            attachment = request.FILES['attachment']
        else:
            attachment = None
        
        submit_obj = Submission.objects.create(connect_sanvriddhi=sanvriddhi_user,session_topic=session_topic,attachment=attachment)
        return redirect(sanvriddhi_dashboard)


@login_required
def sanvriddhi_edit_form(request,pk):
    
    content = get_object_or_404(Sanvriddhi,pk=pk)
    
    if request.method == 'POST':
        form = SanvriddhiEditForm(request.POST,request.FILES,instance=content)
        
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            messages.add_message(request, messages.INFO, 'Edited successfully.')
            return redirect(sanvriddhi_dashboard)
    else:
        form = SanvriddhiEditForm(instance=content)
        
    return render(request,'sanvriddhi_edit_form.html',{'form':form})
