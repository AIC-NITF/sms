from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,JsonResponse
from useraccount.models import Account,Admin,StartUp,TeamMembers,MonitorSheet,WorkGenerator,Forward,Return,TractionSheet,MoM,BlogPost,Query
from .forms import StartUpForm,MonitorSheetEditForm,TractionSheetEditForm

from django.contrib.auth.models import auth
import random
from django.core.mail import send_mail
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
            
            forward_notifications = value.forward_set.filter(new_forward=True).order_by('-date_of_forward')
            return_notifications = Return.objects.filter(to=value,new_return=True).order_by('-return_date')
            total_notifications =  len(forward_notifications) + len(return_notifications)
            
            return_obj = Return.objects.filter(to=value).order_by('-return_date')
            
            return render(request,'emp_dashboard.html',{'value':value,'accounts':accounts,'works':works,'assigned_work':assigned_work,'from_works':from_works,'ford_status':ford_status,'pending_status':pending_status,'completed_status':completed_status,'return_obj':return_obj,'forward_notifications':forward_notifications,'return_notifications':return_notifications,'total_notifications':total_notifications})
        else:
            admin_obj = user.admin_set.all()[0]
            works = admin_obj.workgenerator_set.all().order_by('-date_of_creation')
            assigned_work = admin_obj.forward_set.all().order_by('-date_of_forward')
            
            from_works = Forward.objects.filter(from_user=request.user.fullname).order_by('-date_of_forward')
            
            
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
        values = startup_obj.monitorsheet_set.all().order_by('-date_of_filling')
        traction_values = startup_obj.tractionsheet_set.all().order_by('-generated_date')
        account = Account.objects.filter(is_superadmin=True)[0]
        sendings = MoM.objects.filter(from_user=user.fullname,to=account).order_by('-date_of_creation')
        receving = MoM.objects.filter(from_user=account.fullname,to=user).order_by('-date_of_creation')
        posts = BlogPost.objects.all().order_by('-date_of_creation')
        
        return render(request,'demo_startup_page.html',{'value':startup_obj,'members':val2,'values':values,'traction_values':traction_values,'account':account,'sendings':sendings,'receving':receving,'posts':posts})

@login_required
def visit_startup(request):
    accounts = Account.objects.all()
    return render(request,'startup.html',{'accounts':accounts})

@login_required   
def admin_form(request):
    return render(request,'admin_form.html')

@login_required
def startup_form(request):
    return render(request,'startup_form.html')

@login_required
def profile(request,pk): 
    details = get_object_or_404(Account, pk=pk)
    startup_obj = details.startup_set.all()[0]
    val2 = startup_obj.teammembers_set.all()
    values = startup_obj.monitorsheet_set.all()
    traction_values = startup_obj.tractionsheet_set.all()
    sendings = MoM.objects.filter(from_user=request.user.fullname,to=details).order_by('-date_of_creation')
    receving = MoM.objects.filter(from_user=details.fullname,to=request.user).order_by('-date_of_creation')

    return render(request,'demo_startup_page.html',{'value':startup_obj,'members':val2,'values':values,'traction_values':traction_values,'sendings':sendings,'receving':receving})

@login_required
def startup_profile_edit(request,pk):
    
    content = get_object_or_404(StartUp,pk=pk)
    
    if request.method == 'POST':
        form = StartUpForm(request.POST,instance=content)
        
        if form.is_valid():
            content = form.save(commit=False)
            content.save()
            messages.add_message(request, messages.INFO, 'Edited successfully.')
            return redirect(dashboard)
    else:
        form = StartUpForm(instance=content)
        
    return render(request,'startup_edit_form.html',{'form':form})

@login_required
def delete_employee(request):
    if request.method == 'POST':
        getpk = request.POST['foo']
        
        details = get_object_or_404(Admin,pk=int(getpk))
        main_account = details.account
        
        main_account.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('dashboard')


@login_required
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
        messages.add_message(request, messages.INFO, 'Edited successfully.')
    return redirect('dashboard')
    
#user profile
@login_required
def userprofile(request,pk):
    details = get_object_or_404(Account,pk=pk)
    val = details.admin_set.all()
    return render(request,'user_profile.html',{'value':val[0]})
    
@login_required
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
        messages.add_message(request, messages.INFO, 'One team member added successfully.')
        return redirect('profile',pk=user.pk)
        
@login_required
def delete_team_member(request):
    if request.method == 'POST':
        user = request.user
        getpk = request.POST['foo']
        
        details = get_object_or_404(TeamMembers,pk=int(getpk))
        details.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('profile',pk=user.pk)

@login_required
def edit_team_member(request):

    if request.method == "POST":
        user = request.user
        pk = request.POST['pk_val']
        designation = request.POST['designation']
        email = request.POST['email']
        contact = request.POST['contact']
        
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
        messages.add_message(request, messages.INFO, 'Edited successfully.')
    return redirect('profile',pk=user.pk)


def monitor_report(request,pk):
    monitor_sheet_obj = MonitorSheet.objects.get(pk=pk)
    return render(request,'monitor_report.html',{'monitor_report':monitor_sheet_obj})

@login_required
def allowedit(request,pk):
    monitor_report_obj = MonitorSheet.objects.get(pk=pk)
    monitor_report_obj.allow_edit_option()
    return redirect(monitor_report,pk=pk)


@login_required
def monitor_sheet_edit(request,pk):
    content = get_object_or_404(MonitorSheet,pk=pk)
    
    if request.method == 'POST':
        form = MonitorSheetEditForm(request.POST,instance=content)
        
        if form.is_valid():
            content = form.save(commit=False)
            content.not_allow_edit_option()
            content.update_date()
            content.save()
            messages.add_message(request, messages.INFO, 'Monitor report edited successfully.')
            return redirect(dashboard)
    else:
        form = MonitorSheetEditForm(instance=content)
        
    return render(request,'edit_monitor_sheet.html',{'form':form})

@login_required
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
        
        mou = request.POST['mou']
        
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

        monitor_report = MonitorSheet.objects.create(connect_startup=startup_obj,company_name=company_name,lead_entreprenure=lead_entreprenure,designation=designation,website=website,email=email,contact_no=contact_no,address=address,product_service=product_service,industry=industry,competitors=competitors,incubation_period=incubation_period,chef_monitor=chef_monitor,share_holder_pattern=share_holder_pattern,authorized_capital_amount=authorized_capital_amount,paid_up_capital_amount=paid_up_capital_amount,
                                                      mou=mou,mou_date=mou_date,incubation_fees=incubation_fees,chef_monitor_assign=chef_monitor_assign,ssha_signed=ssha_signed,ssha_date=ssha_date,share_transferred=share_transferred,share_certificates=share_certificates,no_of_seats_taken=no_of_seats_taken,rent_of_seats=rent_of_seats,capital_invested=capital_invested,status_of_registration=status_of_registration,current_traction=current_traction,status_of_product_service=status_of_product_service,status_of_operations=status_of_operations,current_team_member=current_team_member,
                                                      ipr_status=ipr_status,sales=sales,revenue=revenue,pipeline=pipeline,current_client=current_client,profit_earned=profit_earned,new_team_member=new_team_member,no_of_employees=no_of_employees,problem_faced=problem_faced,option=option,marketing=marketing,helped=helped,remarks=remarks,
                                                       name_date=name_date,feture_plan=feture_plan,action=action,required_help=required_help)
        monitor_report.save()
        super_admin = Account.objects.filter(is_superadmin=True)[0]
        obj = super_admin.admin_set.all()[0]
        send_mail(
                'Monitor Report',
                'Monitor report submitted by '+startup_obj.startup_name,
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Monitor Form submitted successfully.')
        return redirect('dashboard')
    else:
        return render(request,'monitor_form.html')

@login_required
def send_mom(request):
    
    if request.method == 'POST' or request.FILES['document']:
        
        from_user = request.POST['from']
        to = request.POST['to']
        title = request.POST['title']
        description = request.POST['description']
        document = request.FILES['document']

        from_obj = Account.objects.get(pk=int(from_user))
        to_obj = Account.objects.get(pk=int(to))
        

        mom_obj = MoM.objects.create(from_user=from_obj.fullname,to=to_obj,title=title,description=description,document=document)
        mom_obj.save()

        

        if request.user.is_superadmin:
            obj = to_obj.startup_set.all()[0]
            send_mail(
                'Minute of Meeting',
                'You receved a MoM by AIC-NITF',
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
            messages.add_message(request, messages.INFO, 'MoM send successfully.')
            return redirect(profile,int(to))
        else:
            name = from_obj.startup_set.all()[0]
            obj = to_obj.admin_set.all()[0]
            send_mail(
                'Minute of Meeting',
                'MoM submitted by '+name.startup_name,
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
            messages.add_message(request, messages.INFO, 'MoM send successfully.')
            return redirect(dashboard)
    else:
        if request.user.is_superadmin:
            return redirect(profile,int(to))
        else:
            return redirect(dashboard)

@login_required
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
        super_admin = Account.objects.filter(is_superadmin=True)[0]
        obj = super_admin.admin_set.all()[0]
        send_mail(
                'Traction Report',
                'Traction report submitted by '+startup_obj.startup_name,
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Traction form submitted successfully.')
        return redirect('dashboard')
    
    else:
        return render(request,'traction_form.html')


def traction_report(request,pk):
    traction_sheet_obj = TractionSheet.objects.get(pk=pk)
    
    return render(request,'traction_report.html',{'traction_report':traction_sheet_obj})

@login_required
def allow_traction_edit(request,pk):
    traction_report_obj = TractionSheet.objects.get(pk=pk)
    traction_report_obj.allow_edit_option()
    return redirect(traction_report,pk=pk)


@login_required
def edit_traction_sheet(request,pk):
    content = get_object_or_404(TractionSheet,pk=pk)
    
    if request.method == 'POST':
        form = TractionSheetEditForm(request.POST,instance=content)
        
        if form.is_valid():
            content = form.save(commit=False)
            content.not_allow_edit_option()
            content.update_date()
            content.save()
            messages.add_message(request, messages.INFO, 'Traction report edited successfully.')
            return redirect(dashboard)
    else:
        form = TractionSheetEditForm(instance=content)
        
    return render(request,'edit_traction_sheet.html',{'form':form})


def blogPost(request):
    posts = BlogPost.objects.all().order_by('-date_of_creation')
    return render(request,'blogPost.html',{'posts':posts})

@login_required
def newBlogPost(request):
    
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        blog_img = request.FILES['blog_img']
        
        post = BlogPost.objects.create(title=title,description=description,blog_img=blog_img)
        post.save()
        messages.add_message(request, messages.INFO, 'Blog posted successfully.')
        return redirect('blogPost')
    

    return redirect('blogPost')

@login_required
def delete_blogPost(request):
    if request.method == 'POST':
        getpk = request.POST['foo']
        details = get_object_or_404(BlogPost,pk=int(getpk))
        details.delete()
        messages.add_message(request, messages.INFO, 'Blog deleted')
    return redirect('blogPost')

@login_required
def edit_blogPost(request):

    if request.method == "POST":
        getpk = request.POST['pk_val']
        title = request.POST['title']
        description = request.POST['description']
        details = get_object_or_404(BlogPost,pk=int(getpk))
        if title:
            title = title
        else:
            title = ' '
        
        if description:
            description = description
        else:
            description = ' '

        details.update_blogPost(title = title,description = description)
    return redirect('blogPost')

def queries(request):
    values = Query.objects.all().order_by('-submitted_date')
    return render(request,'query.html',{'values':values})

@login_required
def delete_query(request):
    if request.method == 'POST':
        getpk = request.POST['foo']
        details = get_object_or_404(Query,pk=int(getpk))
        details.delete()
    return redirect('queries')


@login_required
def generate_work(request):
    
    if request.method == 'POST':
        
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
        
        obj = Admin.objects.get(pk=int(to))
        
        if checkbox:
            work = WorkGenerator.objects.create(from_user=from_obj.fullname,to=obj,title=title,work_description=work_description,suggestions=suggestions,remarks=remarks,document=document,from_user_pk=from_user)
        else:
            work = WorkGenerator.objects.create(from_user=from_obj.fullname,to=obj,title=title,work_description=work_description,suggestions=suggestions,remarks=remarks,from_user_pk=from_user)
        work.change_status(status="Not Started..")

        send_mail(
                'My Work',
                'You got a new work . Please go checkout at www.aicnitf.in .',
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Work Generated successfully.')
        return redirect('dashboard')
    return redirect('index')

@login_required
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
        messages.add_message(request, messages.INFO, 'Work Edited successfully.')
    return redirect('dashboard')


@login_required
def start(request,pk):
    work_obj = WorkGenerator.objects.get(pk=pk)
    work_obj.change_status(status="pending...")
    return redirect('dashboard')

@login_required
def completed(request):
    if request.method == 'POST':
        pk = request.POST['complete_pk']
        ford_pk = request.POST['ford_complete_pk']
        end_statement = request.POST['end_statement']
        checkbox = request.POST.get('upload_checkbox',None)
        if checkbox: 
            end_document = request.FILES['end_document']
        
        if checkbox:
            if ford_pk:
                obj = Forward.objects.get(pk=int(ford_pk))
                obj.forward_work.update_end_msg(end_statement=end_statement +" (work completed by " +obj.to.account.fullname +")",end_document=end_document)
                obj.forward_work.change_status(status="completed")
                obj.forward_work.update_date()
                return redirect('dashboard')
            else:
                work_obj = WorkGenerator.objects.get(pk=int(pk))
                work_obj.update_end_msg(end_statement=end_statement+" work completed by " +work_obj.to.account.fullname,end_document=end_document)
                work_obj.change_status(status="completed")
                work_obj.update_date()
                return redirect('dashboard')
        else:
            if ford_pk:
                obj = Forward.objects.get(pk=int(ford_pk))
                obj.forward_work.update_end_msg(end_statement=end_statement +" (work completed by " +obj.to.account.fullname +")")
                obj.forward_work.change_status(status="completed")
                obj.forward_work.update_date()
                return redirect('dashboard')
            else:
                work_obj = WorkGenerator.objects.get(pk=int(pk))
                work_obj.update_end_msg(end_statement=end_statement+" work completed by " +work_obj.to.account.fullname)
                work_obj.change_status(status="completed")
                work_obj.update_date()
                return redirect('dashboard')
    return redirect('dashboard')

@login_required
def forward_work(request):
    if request.method == 'POST':
        from_user = request.POST['from']
        to = request.POST['to']
        pk = request.POST['pk_val']
        forward_pk = request.POST['pk_val2']
        suggestions = request.POST['suggestions']
        checkbox = request.POST.get('upload_checkbox',None)
        if checkbox: 
            ford_document = request.FILES['ford_document']

        from_obj = Account.objects.get(pk=int(from_user))
        
        obj = Admin.objects.get(pk=int(to))
        
        work_obj = WorkGenerator.objects.get(pk=int(pk))
        
        if checkbox:
            work = Forward.objects.create(from_user=from_obj.fullname,to=obj,forward_work=work_obj,suggestions=suggestions,from_user_pk=from_user,forward_pk=forward_pk,ford_document=ford_document)
        else:
            work = Forward.objects.create(from_user=from_obj.fullname,to=obj,forward_work=work_obj,suggestions=suggestions,from_user_pk=from_user,forward_pk=forward_pk)

        status_obj = WorkGenerator.objects.get(pk=int(pk))
        
        # if status_obj.status == "returned":
        #     ret_obj = Return.objects.get(pk=int(forward_pk))
        #     ret_obj.delete()

        if status_obj.forwarded == False:
            status_obj.forward(from_obj.fullname,obj.account.fullname)
        else:
            for_obj = Forward.objects.get(pk=int(forward_pk))
            for_obj.forther_forward() 
        status_obj.change_status(status="forwarded->")
        work.save()

        fm_ob = from_obj.admin_set.all()[0]
        send_mail(
                'Forwarded Work',
                'you got a work by work ' +from_obj.fullname ,
                fm_ob,
                [obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Work Forwarded successfully.')
        return redirect('dashboard')

@login_required
def return_work(request):
    if request.method == 'POST':
        from_user = request.POST['from']
        to = request.POST['to']
        work_pk = request.POST['work_pk']
        suggestions = request.POST['suggestions']
        ford_work_pk = request.POST['ford_work_pk']
        
        
        from_obj = Account.objects.get(pk=int(from_user))
        
        obj = Account.objects.get(pk=int(to))
        to_obj = obj.admin_set.all()[0]
        
        work_obj = WorkGenerator.objects.get(pk=int(work_pk))
        

        return_obj = Return.objects.create(from_user=from_obj.fullname,to=to_obj,work=work_obj,message=suggestions)

        if work_obj.forwarded:
            ford_obj = Forward.objects.get(pk=int(ford_work_pk))
            
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
        fm_ob = from_obj.admin_set.all()[0] 
        send_mail(
                'Return Work',
                'you receved a return work',
                fm_ob,
                [to_obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Work Returned successfully.')
        return redirect('dashboard')

@login_required
def reassign(request):
    
    if request.method == 'POST':
        from_user = request.POST['from']
        to = request.POST['to']
        work_pk = request.POST['pk_val']
        rk_val = request.POST['rk_val']
        print(work_pk,"======================")
        
        
        obj = Admin.objects.get(pk=int(to))
        
        work_obj = WorkGenerator.objects.get(pk=int(work_pk))
        
        ret = Return.objects.get(pk=int(rk_val))
        
        work_obj.update_to(to=obj)
        work_obj.make_new_work()
        work_obj.change_status(status="Not Started..")
        ret.delete()
        send_mail(
                'My Work',
                'You got a new work . Please go checkout at www.aicnitf.in .',
                'support@aicnalanda.com',
                [obj.email],
                fail_silently=False,
            )
        messages.add_message(request, messages.INFO, 'Work Reassigned successfully.')
        return redirect('dashboard')

@login_required
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

@login_required
def delete_work(request,pk):
    ret_obj = Return.objects.get(pk=pk)
    if request.user.is_adminstrator and ret_obj.work.forwarded == False:
        ret_obj.work.delete()
    else:
        ret_obj.delete()
    return redirect('dashboard')



@login_required
def new_work_clicked(request):
    pk = request.GET.get('pk',None)
    work = WorkGenerator.objects.get(pk=pk)

    work.new_work = False
    work.save()
    data = {
        'new_work':work.new_work
    }
    return JsonResponse(data)

@login_required
def forward_work_clicked(request):
    pk = request.GET.get('pk',None)
    
    work = Forward.objects.get(pk=pk)
    
    work.new_forward = False
    work.save()
    data = {
        'new_work':work.new_forward
    }
    return JsonResponse(data)
@login_required
def return_work_clicked(request):
    pk = request.GET.get('pk',None)
    work = Return.objects.get(pk=pk)
    
    work.new_return = False
    work.save()
    data = {
        'new_work':work.new_return
    }
    return JsonResponse(data)

def return_work_status(request):
    pk = request.GET.get('pk',None)
    work = Return.objects.get(pk=pk)
    data = {
        'new_work':work.new_return
    }
    return JsonResponse(data) 

def new_work_status(request):
    pk = request.GET.get('pk',None)
    work = WorkGenerator.objects.get(pk=pk)
    data = {
        'new_work':work.new_work
    }
    return JsonResponse(data)

def forward_work_status(request):
    pk = request.GET.get('pk',None)
    work = Forward.objects.get(pk=pk)
    data = {
        'new_work':work.new_forward
    }
    return JsonResponse(data)






def count_values(request):
    returns = Return.objects.filter(work__new_work = True)
    
    data = {
        'returns':len(returns)
    }
    return JsonResponse(data)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/document")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


def verify_uname(request):
    uname = request.GET.get('uname',None)
    data = {
        'exist': Account.objects.filter(username = uname).exists(),
    }
    return JsonResponse(data)

def uname_pwd_check(request):
    uname = request.GET.get('uname',None)
    pwd = request.GET.get('pwd',None)
    user = auth.authenticate(request,username=uname,password=pwd)
    exist = False
    if user is not None:
        exist = True
    
    else:
        exist = False

    
    data = {
        'exist':exist
    }
    return JsonResponse(data)

def forget_username(request):
    uname = request.GET.get('uname',None)
    user = Account.objects.filter(username=uname).first()
    if user is not None:
        if user.is_admin:
            admin = user.admin_set.first()
            email = admin.email
        if user.is_startup:
            startup = user.startup_set.first()
            email = startup.email
    else:
        email = None
    data = {
        'is_exist': Account.objects.filter(username=uname).exists(),
        'email':email
    }
    

    return JsonResponse(data)


def forget_email_sending(request):
    email = request.GET.get('email',None)
    num_list = ['1','2','3','4','5','6','7','8','9']
    otp = random.sample(num_list,4)
    str_otp = ''.join(otp)
    
    send_mail(
    'Password Reset OTP',
    'Your one time password to reset AICNITF account is :{0}'.format(str_otp),
    'support@aicnalanda.com',
    [email],
    fail_silently=False,
    )
    data = {
        'correct_otp':str_otp
    }
    return JsonResponse(data)


def set_password(request):
    password = request.GET.get('password',None)
    uname = request.GET.get('username',None)
    user = Account.objects.get(username=uname)
   
    user.set_password(password)
    user.save()
    data = {
        'uname':uname
    }
    return JsonResponse(data)


