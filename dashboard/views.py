from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from useraccount.models import Account,Admin,StartUp,TeamMembers,MonitorSheet,WorkGenerator,Forward
from .forms import StartUpForm,MonitorSheetEditForm
from django.core.files.storage import FileSystemStorage


# Create your views here.
def dashboard(request):
    accounts = Account.objects.all()
    user = request.user
    admins = Admin.objects.all()
    if user.is_superadmin:
        return render(request,'startup.html',{'accounts':accounts})
    elif user.is_admin:
        value = user.admin_set.all()[0]
        if user.is_adminstrator:
            works = WorkGenerator.objects.all().order_by('-date_of_creation')
            return render(request,'emp_dashboard.html',{'value':value,'accounts':accounts,'works':works})
        else:
            admin_obj = user.admin_set.all()[0]
            works = admin_obj.workgenerator_set.all().order_by('-date_of_creation')
            forwardwork = admin_obj.forward_set.all()
            print(works,"`````````````````````````")
            return render(request,'emp_dashboard.html',{'value':value,'accounts':accounts,'works':works,'forwardwork':forwardwork})        
        
    else:
        user = request.user
        startup_obj = user.startup_set.all()[0]
        val2 = startup_obj.teammembers_set.all()
        values = startup_obj.monitorsheet_set.all()
        print(user)
        print(user.pk)
        print(startup_obj)
        print(val2)
        print(values)
        return render(request,'demo_startup_page.html',{'value':startup_obj,'members':val2,'values':values})

def visit_startup(request):
    accounts = Account.objects.all()
    return render(request,'startup.html',{'accounts':accounts})

def visit_employee(request,pk):
    value = Admin.objects.get(pk=pk)
    print(pk,"-------------------")
    if value.account.is_adminstrator:
        works = WorkGenerator.objects.all().order_by('-date_of_creation')
        return render(request,'emp_dashboard.html',{'value':value,'works':works})
    else:
        works = value.workgenerator_set.all().order_by('-date_of_creation')
        print(works,"`````````````````````````")
        return render(request,'emp_dashboard.html',{'value':value,'works':works})
    
    

def admin_form(request):
    return render(request,'admin_form.html')

def startup_form(request):
    return render(request,'startup_form.html')

def profile(request,pk): 
    details = get_object_or_404(Account, pk=pk)
    startup_obj = details.startup_set.all()[0]
    val2 = startup_obj.teammembers_set.all()
    values = startup_obj.monitorsheet_set.all()
    
    print("=====================================================================")
    return render(request,'demo_startup_page.html',{'value':startup_obj,'members':val2,'values':values})

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

def delete_employee(request):
    if request.method == 'POST':
        getpk = request.POST['foo']
        print(getpk)
        details = get_object_or_404(Admin,pk=int(getpk))
        main_account = details.account
        print(main_account)
        main_account.delete()
        return redirect('dashboard')



def edit_emp_form(request):

    if request.method == "POST":
        pk = request.POST['pk_val']
        designation = request.POST['designation']
        email = request.POST['email']
        contact = request.POST['contact']

        account = Admin.objects.get(pk=pk)

        if designation:
            designation = designation
        else:
            designation = ' '
        
        if email:
            email = email
        else:
            email = ' '

        if contact:
            contact = contact
        else:
            contact = ' '

        account.update_admin(email = email,designation = designation,contact_no = contact)
    return redirect('dashboard')
    
#user profile
def userprofile(request,pk):
    details = get_object_or_404(Account,pk=pk)
    print(details)
    if details.is_superadmin:
        return render(request,'user_profile.html',{'value':details})
    elif details.is_admin:
        val = details.admin_set.all()
        print(val)
        return render(request,'user_profile.html',{'value':val[0]})
    else:
        return redirect('profile',pk=pk)

def add_new_team_member(request):
    if request.method == 'POST':
        user = request.user
        startup_obj = user.startup_set.all()[0]
        name = request.POST['name']
        gender = request.POST['gender']
        email = request.POST['email']
        contact_no = request.POST['contact']
        designation = request.POST['designation']

        team_member = TeamMembers.objects.create(startup=startup_obj,name=name,gender=gender,email=email,contact_no=contact_no,designation=designation)
        team_member.save()
        return redirect('profile',pk=user.pk)
        

def delete_team_member(request):
    if request.method == 'POST':
        user = request.user
        getpk = request.POST['foo']
        print(getpk)
        details = get_object_or_404(TeamMembers,pk=int(getpk))
        details.delete()
        return redirect('profile',pk=user.pk)

def edit_team_member(request):

    if request.method == "POST":
        user = request.user
        pk = request.POST['pk_val']
        designation = request.POST['designation']
        email = request.POST['email']
        contact = request.POST['contact']
        print(pk,"=============================================")
        account = TeamMembers.objects.get(pk=pk)

        if designation:
            designation = designation
        else:
            designation = ' '
        
        if email:
            email = email
        else:
            email = ' '

        if contact:
            contact = contact
        else:
            contact = ' '

        account.update_team_member(email = email,designation = designation,contact_no = contact)
    return redirect('profile',pk=user.pk)

def monitor_report(request,pk):
    monitor_sheet_obj = MonitorSheet.objects.get(pk=pk)
    print(monitor_sheet_obj,"+++++++++++++++++++++++++++++++++++++")
    return render(request,'monitor_report.html',{'monitor_report':monitor_sheet_obj})

def allowedit(request,pk):
    monitor_report_obj = MonitorSheet.objects.get(pk=pk)
    print(monitor_report_obj.allow_edit)
    monitor_report_obj.allow_edit_option()
    print(monitor_report_obj.allow_edit)
    return redirect(monitor_report,pk=pk)



def monitor_sheet_edit(request,pk):
    content = get_object_or_404(MonitorSheet,pk=pk)
    print(content)
    if request.method == 'POST':
        form = MonitorSheetEditForm(request.POST,instance=content)
        print(form) 
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            content.not_allow_edit_option()
            return redirect(dashboard)
    else:
        form = MonitorSheetEditForm(instance=content)
        print(form," form")
    return render(request,'edit_monitor_sheet.html',{'form':form})






def monitor_sheet(request):
    user = request.user
    if user.is_startup:
        startup_obj = user.startup_set.all()[0]
        values = startup_obj.monitorsheet_set.all()
        return render(request,'monitor_sheet.html',{'values':values})
    return render(request,'traction_sheet.html')

def traction_sheet(request):
    return render(request,'traction_sheet.html')


def minute_of_meeting(request):
    return render(request,'minute_of_meeting.html')




def monitor_form(request):
    if request.method == 'POST':
        user = request.user
        startup_obj = user.startup_set.all()[0]

        company_name = request.POST['company_name']
        lead_entreprenure = request.POST['lead_entreprenure']
        designation = request.POST['designation']
        website = request.POST['website']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        address = request.POST['address']
        product_service = request.POST['product_service']
        industry = request.POST['industry']
        competitors = request.POST['competitors']
        incubation_period = request.POST['incubation_period']
        chef_monitor = request.POST['chef_monitor']
        share_holder_pattern = request.POST['share_holder_pattern']
        authorized_capital_amount = request.POST['authorized_capital_amount']
        paid_up_capital_amount = request.POST['paid_up_capital_amount']
        date_of_filling = request.POST['date_of_filling']
        
        mou = request.POST['mou']
        print(mou,"-------------------------------------------------")
        mou_date = request.POST['mou_date']
        incubation_fees = request.POST['incubation_fees']
        chef_monitor_assign = request.POST['chef_monitor_assign']
        ssha_signed = request.POST['ssha_signed']
        ssha_date = request.POST['ssha_date']
        share_transferred = request.POST['share_transferred']
        share_certificates = request.POST['share_certificates']
        no_of_seats_taken = request.POST['no_of_seats_taken']
        rent_of_seats = request.POST['rent_of_seats']
        capital_invested = request.POST['capital_invested']
        status_of_registration = request.POST['status_of_registration']
        current_traction = request.POST['current_traction']
        status_of_product_service = request.POST['status_of_product_service']
        status_of_operations = request.POST['status_of_operations']
        current_team_member = request.POST['current_team_member']
        
        ipr_status = request.POST['ipr_status']
        sales = request.POST['sales']
        revenue = request.POST['revenue']
        pipeline = request.POST['pipeline']
        current_client = request.POST['current_client']
        profit_earned = request.POST['profit_earned']
        new_team_member = request.POST['new_team_member']
        no_of_employees = request.POST['no_of_employees']
        problem_faced = request.POST['problem_faced']
        option = request.POST['option']
        marketing = request.POST['marketing']
        helped = request.POST['helped']
        remarks = request.POST['remarks']

        name_date = request.POST['name_date']
        feture_plan = request.POST['feture_plan']
        action = request.POST['action']
        required_help = request.POST['required_help']

        monitor_report = MonitorSheet.objects.create(connect_startup=startup_obj,company_name=company_name,lead_entreprenure=lead_entreprenure,designation=designation,website=website,email=email,contact_no=contact_no,address=address,product_service=product_service,industry=industry,competitors=competitors,incubation_period=incubation_period,chef_monitor=chef_monitor,share_holder_pattern=share_holder_pattern,authorized_capital_amount=authorized_capital_amount,paid_up_capital_amount=paid_up_capital_amount,date_of_filling=date_of_filling,
                                                      mou=mou,mou_date=mou_date,incubation_fees=incubation_fees,chef_monitor_assign=chef_monitor_assign,ssha_signed=ssha_signed,ssha_date=ssha_date,share_transferred=share_transferred,share_certificates=share_certificates,no_of_seats_taken=no_of_seats_taken,rent_of_seats=rent_of_seats,capital_invested=capital_invested,status_of_registration=status_of_registration,current_traction=current_traction,status_of_product_service=status_of_product_service,status_of_operations=status_of_operations,current_team_member=current_team_member,
                                                      ipr_status=ipr_status,sales=sales,revenue=revenue,pipeline=pipeline,current_client=current_client,profit_earned=profit_earned,new_team_member=new_team_member,no_of_employees=no_of_employees,problem_faced=problem_faced,option=option,marketing=marketing,helped=helped,remarks=remarks,
                                                       name_date=name_date,feture_plan=feture_plan,action=action,required_help=required_help)
        monitor_report.save()
        return redirect('dashboard')
    else:
        return render(request,'monitor_form.html')






def generate_work(request):
    
    if request.method == 'POST' or request.FILES['document']:

        fs = FileSystemStorage()
        if request.FILES['document']:
            doc = request.FILES['document']
            file_name = fs.save(doc.name,doc)
            file_url = fs.url(file_name)
        
        if file_name:
            pass
        else:
            file_name = ''
        
        from_user = request.POST['from']
        to = request.POST['to']
        title = request.POST['title']
        work_description = request.POST['work_description']
        suggestions = request.POST['suggestions']
        remarks = request.POST['remarks']
        #document = request.FILES['document']
        
        from_obj = Account.objects.get(pk=int(from_user))
        print(from_obj.fullname)
        obj = Admin.objects.get(pk=int(to))
        print(obj,"=====================")
        work = WorkGenerator.objects.create(from_user=from_obj.fullname,to=obj,title=title,work_description=work_description,suggestions=suggestions,remarks=remarks,document=file_name)
        work.change_status(status="Not Started..")
        return redirect('dashboard')
    return redirect('index')

def edit_work(request):
    if request.method == "POST":
        pk = request.POST['pk_val']
        title = request.POST['title']
        work_description = request.POST['work_description']
        suggestions = request.POST['suggestions']
        remarks = request.POST['remarks']

        work_obj = WorkGenerator.objects.get(pk=pk)

        if title:
            title = title
        else:
            title = ' '
        
        if work_description:
            work_description = work_description
        else:
            work_description = ' '

        if suggestions:
            suggestions = suggestions
        else:
            suggestions = ' '
        
        if remarks:
            remarks = remarks
        else:
            remarks = ' '

        work_obj.update_work(title = title,work_description = work_description,suggestions = suggestions,remarks=remarks)
    return redirect('dashboard')



def start(request,pk):
    work_obj = WorkGenerator.objects.get(pk=pk)
    work_obj.change_status(status="pending...")
    return redirect('dashboard')

def completed(request,pk):
    work_obj = WorkGenerator.objects.get(pk=pk)
    work_obj.change_status(status="completed")
    work_obj.update_date()
    return redirect('dashboard')

def forward_work(request):
    if request.method == 'POST':
        from_user = request.POST['from']
        to = request.POST['to']
        pk = request.POST['pk_val']
        suggestions = request.POST['suggestions']

        from_obj = Account.objects.get(pk=int(from_user))
        print(from_obj.fullname)
        obj = Admin.objects.get(pk=int(to))
        print(obj,"=====================")
        work_obj = WorkGenerator.objects.get(pk=int(pk))
        print(work_obj,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        work = Forward.objects.create(from_user=from_obj.fullname,to=obj,forward_work=work_obj,suggestions=suggestions)
        status_obj = WorkGenerator.objects.get(pk=int(pk))
        print(obj.account.fullname)
        status_obj.forward(from_obj.fullname,obj.account.fullname)
        status_obj.change_status(status="forwarded->")
        work.save()
        return redirect('dashboard')


# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/document")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404