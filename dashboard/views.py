from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from useraccount.models import Account,Admin,StartUp,TeamMembers,MonitorSheet,WorkGenerator,Forward,Return,TractionSheet,MoM,BlogPost
from .forms import StartUpForm,MonitorSheetEditForm,TractionSheetEditForm,BlogPostForm
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
            ford_status = WorkGenerator.objects.filter(forwarded=True).order_by('-date_of_creation')
            pending_status = WorkGenerator.objects.filter(status='pending...').order_by('-date_of_creation')
            completed_status = WorkGenerator.objects.filter(status='completed').order_by('-date_of_creation')
            assigned_work = value.forward_set.all().order_by('-date_of_forward')
            from_works = Forward.objects.filter(from_user=request.user.fullname).order_by('-date_of_forward')
            print(ford_status)
            return_obj = Return.objects.filter(to=value).order_by('-return_date')
            print(return_obj)
            return render(request,'emp_dashboard.html',{'value':value,'accounts':accounts,'works':works,'assigned_work':assigned_work,'from_works':from_works,'ford_status':ford_status,'pending_status':pending_status,'completed_status':completed_status,'return_obj':return_obj})
        else:
            admin_obj = user.admin_set.all()[0]
            works = admin_obj.workgenerator_set.all().order_by('-date_of_creation')
            assigned_work = admin_obj.forward_set.all().order_by('-date_of_forward')
            print(works,"`````````````````````````")
            from_works = Forward.objects.filter(from_user=request.user.fullname).order_by('-date_of_forward')
            print(from_works)
            
            pending_status = admin_obj.workgenerator_set.filter(status='pending...').order_by('-date_of_creation')
            completed_status = admin_obj.workgenerator_set.filter(status='completed').order_by('-date_of_creation')
            val = admin_obj.forward_set.filter(to=admin_obj).order_by('-date_of_forward')
            assign_pending_status = []
            for v in val:
                if v.forward_work.status == "pending...":
                    assign_pending_status.append(v)
            assign_completed_status = []
            for v in val:
                if v.forward_work.status == "completed":
                    assign_completed_status.append(v)
            return_obj = Return.objects.filter(to=value).order_by('-return_date')

            work_notifications = admin_obj.workgenerator_set.filter(new_work=True).order_by('-date_of_creation')
            forward_notifications = admin_obj.forward_set.filter(new_forward=True).order_by('-date_of_forward')
            return_notifications = Return.objects.filter(to=value,new_return=True).order_by('-return_date')
            total_notifications = len(work_notifications) + len(forward_notifications) + len(return_notifications)
            return render(request,'emp_dashboard.html',{'value':value,'accounts':accounts,'works':works,'assigned_work':assigned_work,'from_works':from_works,'pending_status':pending_status,'assign_pending_status':assign_pending_status,'completed_status':completed_status,'assign_completed_status':assign_completed_status,'return_obj':return_obj,'work_notifications':work_notifications,'forward_notifications':forward_notifications,'return_notifications':return_notifications,'total_notifications':total_notifications})        
        
    else:
        user = request.user
        startup_obj = user.startup_set.all()[0]
        val2 = startup_obj.teammembers_set.all()
        values = startup_obj.monitorsheet_set.all()
        traction_values = startup_obj.tractionsheet_set.all()
        account = Account.objects.filter(is_superadmin=True)[0]
        sendings = MoM.objects.filter(from_user=user.fullname,to=account).order_by('-date_of_creation')
        receving = MoM.objects.filter(from_user=account.fullname,to=user).order_by('-date_of_creation')
        print(sendings)
        print(receving)
        print(account)
        print(user)
        print(user.pk)
        print(startup_obj)
        print(val2)
        print(values)
        return render(request,'demo_startup_page.html',{'value':startup_obj,'members':val2,'values':values,'traction_values':traction_values,'account':account,'sendings':sendings,'receving':receving})

def visit_startup(request):
    accounts = Account.objects.all()
    return render(request,'startup.html',{'accounts':accounts})

def visit_employee(request,pk):
    value = Admin.objects.get(pk=pk)
    print(pk,"-------------------")
    if value.account.is_adminstrator:
        works = WorkGenerator.objects.all().order_by('-date_of_creation')
        ford_status = WorkGenerator.objects.filter(forwarded=True).order_by('-date_of_creation')
        print(ford_status,"....................................................")
        return render(request,'emp_dashboard.html',{'value':value,'works':works,'ford_status':ford_status})
    else:
        works = value.workgenerator_set.all().order_by('-date_of_creation')
        forwardwork = value.forward_set.all().order_by('-date_of_forward')
        from_works = Forward.objects.filter(from_user=value.account.fullname).order_by('-date_of_forward')
        print(works,"`````````````````````````")
        return render(request,'emp_dashboard.html',{'value':value,'works':works,'forwardwork':forwardwork,'from_works':from_works})
    
    

def admin_form(request):
    return render(request,'admin_form.html')

def startup_form(request):
    return render(request,'startup_form.html')

def profile(request,pk): 
    details = get_object_or_404(Account, pk=pk)
    startup_obj = details.startup_set.all()[0]
    val2 = startup_obj.teammembers_set.all()
    values = startup_obj.monitorsheet_set.all()
    traction_values = startup_obj.tractionsheet_set.all()
    sendings = MoM.objects.filter(from_user=request.user.fullname,to=details).order_by('-date_of_creation')
    receving = MoM.objects.filter(from_user=details.fullname,to=request.user).order_by('-date_of_creation')

    
    print("=====================================================================")
    return render(request,'demo_startup_page.html',{'value':startup_obj,'members':val2,'values':values,'traction_values':traction_values,'sendings':sendings,'receving':receving})

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

def send_mom(request):
    print("helllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllo")
    if request.method == 'POST' or request.FILES['document']:
        print("helooooooooooooooooooo")
        from_user = request.POST['from']
        to = request.POST['to']
        title = request.POST['title']
        description = request.POST['description']
        document = request.FILES['document']

        from_obj = Account.objects.get(pk=int(from_user))
        to_obj = Account.objects.get(pk=int(to))
        print(to_obj)

        mom_obj = MoM.objects.create(from_user=from_obj.fullname,to=to_obj,title=title,description=description,document=document)
        mom_obj.save()

        if request.user.is_superadmin:
            return redirect(profile,int(to))
        else:
            return redirect(dashboard)
    else:
        if request.user.is_superadmin:
            return redirect(profile,int(to))
        else:
            return redirect(dashboard)

def traction_form(request):
    if request.method == 'POST':
        user = request.user
        startup_obj = user.startup_set.all()[0]

        total_order     = request.POST['total_order']
        average_packet_size   = request.POST['average_packet_size']
        total_revenue_of_month  = request.POST['total_revenue_of_month']
        total_customers_served  = request.POST['total_customers_served']
        total_expense     = request.POST['total_expense']
        market_outreach   = request.POST['market_outreach']
        repeate_customers    = request.POST['repeate_customers']
        total_revenue     = request.POST['total_revenue']
        direct_job_created   = request.POST['direct_job_created']
        indirect_job_created   = request.POST['indirect_job_created']
        profit = request.POST['profit']

        traction_report = TractionSheet.objects.create(connect_startup=startup_obj,total_order=total_order,average_packet_size=average_packet_size,total_revenue_of_month=total_revenue_of_month,total_customers_served=total_customers_served,total_expense=total_expense,market_outreach=market_outreach,repeate_customers=repeate_customers,total_revenue=total_revenue,direct_job_created=direct_job_created,indirect_job_created=indirect_job_created,profit=profit)
        return redirect('dashboard')
    
    else:
        return render(request,'traction_form.html')

def traction_report(request,pk):
    traction_sheet_obj = TractionSheet.objects.get(pk=pk)
    print(traction_sheet_obj,"+++++++++++++++++++++++++++++++++++++")
    return render(request,'traction_report.html',{'traction_report':traction_sheet_obj})

def allow_traction_edit(request,pk):
    traction_report_obj = TractionSheet.objects.get(pk=pk)
    traction_report_obj.allow_edit_option()
    return redirect(traction_report,pk=pk)

def edit_traction_sheet(request,pk):
    content = get_object_or_404(TractionSheet,pk=pk)
    print(content)
    if request.method == 'POST':
        form = TractionSheetEditForm(request.POST,instance=content)
        print(form) 
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            content.not_allow_edit_option()
            return redirect(dashboard)
    else:
        form = TractionSheetEditForm(instance=content)
        print(form," form")
    return render(request,'edit_traction_sheet.html',{'form':form})

def blogPost(request):
    posts = BlogPost.objects.all().order_by('-date_of_creation')
    return render(request,'blogPost.html',{'posts':posts})

def newBlogPost(request):
    print("0.0.................0000000000000.000000000000")
    # if request.method == "POST":
    #     form = BlogPostForm(request.POST)
    #     if form.is_valid():
    #         print(form,"...333333333333333..........3333333333")
    #         post = form.save(commit=False)
    #         post.save()
    #         return redirect('blogPost')
    # else:
    #     form = BlogPostForm()
    #     print(form)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        blog_img = request.FILES['blog_img']
        print(blog_img)
        post = BlogPost.objects.create(title=title,description=description,blog_img=blog_img)
        post.save()
        return redirect('blogPost')
    

    return redirect('blogPost')

def generate_work(request):
    
    if request.method == 'POST':

        # fs = FileSystemStorage()
        # if request.FILES['document']:
        #     doc = request.FILES['document']
        #     file_name = fs.save(doc.name,doc)
        #     file_url = fs.url(file_name)
        
        # if file_name:
        #     pass
        # else:
        #     file_name = ''
        
        from_user = request.POST['from']
        to = request.POST['to']
        title = request.POST['title']
        work_description = request.POST['work_description']
        suggestions = request.POST['suggestions']
        remarks = request.POST['remarks']
        checkbox = request.POST.get('upload_checkbox',None)
        if checkbox: 
            document = request.FILES['document']
        
        from_obj = Account.objects.get(pk=int(from_user))
        print(from_obj.fullname)
        obj = Admin.objects.get(pk=int(to))
        print(obj,"=====================")
        if checkbox:
            work = WorkGenerator.objects.create(from_user=from_obj.fullname,to=obj,title=title,work_description=work_description,suggestions=suggestions,remarks=remarks,document=document,from_user_pk=from_user)
        else:
            work = WorkGenerator.objects.create(from_user=from_obj.fullname,to=obj,title=title,work_description=work_description,suggestions=suggestions,remarks=remarks,from_user_pk=from_user)
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
        forward_pk = request.POST['pk_val2']
        suggestions = request.POST['suggestions']

        from_obj = Account.objects.get(pk=int(from_user))
        print(from_obj.fullname)
        obj = Admin.objects.get(pk=int(to))
        print(forward_pk,"=====================")
        work_obj = WorkGenerator.objects.get(pk=int(pk))
        print(work_obj,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        work = Forward.objects.create(from_user=from_obj.fullname,to=obj,forward_work=work_obj,suggestions=suggestions,from_user_pk=from_user,forward_pk=forward_pk)
        status_obj = WorkGenerator.objects.get(pk=int(pk))
        print(obj.account.fullname)
        if status_obj.status == "returned":
            ret_obj = Return.objects.get(pk=int(forward_pk))
            ret_obj.delete()

        if status_obj.forwarded == False:
            status_obj.forward(from_obj.fullname,obj.account.fullname)
        else:
            for_obj = Forward.objects.get(pk=int(forward_pk))
            for_obj.forther_forward() 
        status_obj.change_status(status="forwarded->")
        
        work.save()
        return redirect('dashboard')

def return_work(request):
    if request.method == 'POST':
        from_user = request.POST['from']
        to = request.POST['to']
        work_pk = request.POST['work_pk']
        suggestions = request.POST['suggestions']
        ford_work_pk = request.POST['ford_work_pk']
        print(ford_work_pk)
        print(to,"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        from_obj = Account.objects.get(pk=int(from_user))
        print(from_obj,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.")
        obj = Account.objects.get(pk=int(to))
        to_obj = obj.admin_set.all()[0]
        print(to_obj,"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        work_obj = WorkGenerator.objects.get(pk=int(work_pk))

        return_obj = Return.objects.create(from_user=from_obj.fullname,to=to_obj,work=work_obj,message=suggestions)

        if work_obj.forwarded:
            ford_obj = Forward.objects.get(pk=int(ford_work_pk))
            print(ford_obj)
            return_obj.assign_forward_pk(forward_pk=ford_obj.forward_pk)
            if ford_obj.forward_pk:
                old_ford_obj = Forward.objects.get(pk=ford_obj.forward_pk)
                old_ford_obj.remove_forward()
            else:
                work_obj.remove_forward()
            ford_obj.delete()
        else:
            work_obj.make_null()
        work_obj.change_status(status="returned")
        return_obj.save()
        return redirect('dashboard')

def reassign(request):
    print(".....................................................................")
    if request.method == 'POST':
        from_user = request.POST['from']
        to = request.POST['to']
        work_pk = request.POST['pk_val']
        suggestions = request.POST['suggestions']
        rk_val = request.POST['rk_val']
        print(to,"/////////////////////////////////////////")
        
        obj = Admin.objects.get(pk=int(to))
        work_obj = WorkGenerator.objects.get(pk=int(work_pk))
        ret = Return.objects.get(pk=int(rk_val))
        work_obj.update_to(to=obj)
        work_obj.change_status(status="Not Started..")
        ret.delete()
        return redirect('dashboard')

def return_start(request,pk):
    ret_obj = Return.objects.get(pk=pk)
    if ret_obj.forward_pk:
        ford_obj = Forward.objects.get(pk=int(ret_obj.forward_pk))
        ford_obj.forward_work.change_status(status="pending...")
        ford_obj.remove_forward()
    else:
        work_obj = ret_obj.work
        work_obj.change_status(status="pending...")
        work_obj.remove_forward()
    ret_obj.delete()
    return redirect('dashboard')

def delete_work(request,pk):
    ret_obj = Return.objects.get(pk=pk)
    if request.user.is_adminstrator and ret_obj.work.forwarded == False:
        ret_obj.work.delete()
    else:
        ret_obj.delete()
    return redirect('dashboard')



def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/document")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404