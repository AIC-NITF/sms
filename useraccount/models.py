from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class MyAccountManager(BaseUserManager):
	def create_user(self, username, password=None,**kwargs):
		# if not email:
		# 	raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			#email=self.normalize_email(email),
			username=username,**kwargs
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, password):
		user = self.create_user(
			#email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	fullname 				= models.CharField(max_length=50)
	username 				= models.CharField(max_length=30, unique=True)
	password 				= models.CharField(max_length=100)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)
	is_superadmin 			= models.BooleanField(default=False)
	is_startup 				= models.BooleanField(default=False)
	is_adminstrator			= models.BooleanField(default=False)
	




	USERNAME_FIELD = 'username'

	objects = MyAccountManager()

	def __str__(self):
		return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True



class Admin(models.Model):
	account 				= models.ForeignKey(Account, on_delete=models.CASCADE)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	designation				= models.CharField(max_length=100,null=True,blank=True)
	employee_id				= models.CharField(max_length=100,null=True,blank=True)
	contact_no				= models.CharField(max_length=100,null=True,blank=True)
	identity_proof			= models.CharField(max_length=100,null=True,blank=True)
	admin_img				= models.ImageField(upload_to='images/',null=True,blank=True)

	

	def __str__(self):
		return self.designation

	def update_admin(self,email,designation,contact_no):
		self.email = email
		self.designation = designation
		self.contact_no = contact_no
		self.save()

class StartUp(models.Model):
	account 				= models.ForeignKey(Account, on_delete=models.CASCADE)
	email 					= models.EmailField(verbose_name="email", max_length=60,null=True,blank=True)
	startup_name			= models.CharField(max_length=100,null=True,blank=True)
	legal_entity			= models.CharField(max_length=100,null=True,blank=True)
	founders_designation	= models.CharField(max_length=2000,null=True,blank=True)
	website					= models.CharField(max_length=100,null=True,blank=True)
	city					= models.CharField(max_length=100,null=True,blank=True)
	sector					= models.CharField(max_length=100,null=True,blank=True)
	team_members			= models.CharField(max_length=100,null=True,blank=True)
	location				= models.CharField(max_length=100,null=True,blank=True)
	contact_no				= models.CharField(max_length=100,null=True,blank=True)

	comp_identification_no  = models.CharField(max_length=100,null=True,blank=True)
	inubatee_level			= models.CharField(max_length=100,null=True,blank=True)
	operational_model		= models.CharField(max_length=100,null=True,blank=True)
	type_of_incubatee      	= models.CharField(max_length=50,null=True,blank=True)
	women_led_startup 		= models.CharField(max_length=10,null=True,blank=True)
	gov_program 			= models.CharField(max_length=100,null=True,blank=True)
	msme_registered			= models.CharField(max_length=10,null=True,blank=True)
	dspp_registered			= models.CharField(max_length=10,null=True,blank=True)
	legal_entity_register   = models.CharField(max_length=100,null=True,blank=True)
	startup_img				= models.ImageField(upload_to='images/',null=True,blank=True)
	founder_img				= models.ImageField(upload_to='images/',null=True,blank=True)

	def __str__(self):
		return self.startup_name
    

class TeamMembers(models.Model):
	startup  				= models.ForeignKey(StartUp, on_delete=models.CASCADE)
	name 					= models.CharField(max_length=100,null=True,blank=True)
	gender 					= models.CharField(max_length=10,null=True,blank=True)
	email 					= models.CharField(max_length=100,null=True,blank=True)
	contact_no 				= models.CharField(max_length=200,null=True,blank=True)
	designation				= models.CharField(max_length=200,null=True,blank=True)


	def __str__(self):
		return self.startup.startup_name +" " +self.email
	
	def update_team_member(self,email,designation,contact_no):
		self.email = email
		self.designation = designation
		self.contact_no = contact_no
		self.save()




class MonitorSheet(models.Model):
	connect_startup			      	= models.ForeignKey(StartUp, on_delete=models.CASCADE)
	company_name					= models.CharField(max_length=100,null=True,blank=True)
	lead_entreprenure				= models.CharField(max_length=100,null=True,blank=True)
	designation 					= models.CharField(max_length=100,null=True,blank=True)
	address 						= models.CharField(max_length=2000,null=True,blank=True)
	website 						= models.CharField(max_length=100,null=True,blank=True)
	email							= models.CharField(max_length=100,null=True,blank=True)
	contact_no						= models.CharField(max_length=20,null=True,blank=True)
	product_service					= models.CharField(max_length=200,null=True,blank=True)
	industry						= models.CharField(max_length=200,null=True,blank=True)
	competitors						= models.CharField(max_length=200,null=True,blank=True)
	incubation_period				= models.CharField(max_length=200,null=True,blank=True)
	chef_monitor					= models.CharField(max_length=200,null=True,blank=True)
	share_holder_pattern			= models.CharField(max_length=200,null=True,blank=True)
	authorized_capital_amount		= models.CharField(max_length=200,null=True,blank=True)
	paid_up_capital_amount			= models.CharField(max_length=200,null=True,blank=True)
	date_of_filling					= models.DateTimeField(verbose_name='date of filling', auto_now_add=True,null=True,blank=True)
	
	mou								= models.CharField(max_length=200,null=True,blank=True)
	incubation_fees					= models.CharField(max_length=200,null=True,blank=True)
	chef_monitor_assign				= models.CharField(max_length=200,null=True,blank=True)
	ssha_signed						= models.CharField(max_length=20,null=True,blank=True)
	share_transferred				= models.CharField(max_length=200,null=True,blank=True)
	share_certificates				= models.CharField(max_length=200,null=True,blank=True)
	no_of_seats_taken				= models.CharField(max_length=200,null=True,blank=True)
	rent_of_seats					= models.CharField(max_length=200,null=True,blank=True)
	capital_invested				= models.CharField(max_length=200,null=True,blank=True)
	status_of_registration			= models.CharField(max_length=200,null=True,blank=True)
	current_traction				= models.CharField(max_length=200,null=True,blank=True)
	status_of_product_service 		= models.CharField(max_length=200,null=True,blank=True)
	status_of_operations 			= models.CharField(max_length=200,null=True,blank=True)
	current_team_member 			= models.CharField(max_length=200,null=True,blank=True)
	mou_date 						= models.CharField(max_length=50,null=True,blank=True)
	ssha_date 						= models.CharField(max_length=50,null=True,blank=True)
	
	ipr_status 						= models.CharField(max_length=200,null=True,blank=True)
	sales 							= models.CharField(max_length=200,null=True,blank=True)
	revenue 						= models.CharField(max_length=200,null=True,blank=True)
	pipeline 						= models.CharField(max_length=200,null=True,blank=True)
	current_client 					= models.CharField(max_length=200,null=True,blank=True)
	profit_earned 					= models.CharField(max_length=200,null=True,blank=True)
	new_team_member 				= models.CharField(max_length=200,null=True,blank=True)
	no_of_employees 				= models.CharField(max_length=200,null=True,blank=True)
	problem_faced 					= models.CharField(max_length=200,null=True,blank=True)
	option 							= models.CharField(max_length=200,null=True,blank=True)
	marketing 						= models.CharField(max_length=2000,null=True,blank=True)
	helped 							= models.CharField(max_length=2000,null=True,blank=True)
	remarks 						= models.CharField(max_length=2000,null=True,blank=True)
	
	name_date 						= models.CharField(max_length=200,null=True,blank=True)
	feture_plan 					= models.CharField(max_length=2000,null=True,blank=True)
	action 							= models.CharField(max_length=2000,null=True,blank=True)
	required_help 					= models.CharField(max_length=2000,null=True,blank=True)

	allow_edit 						= models.BooleanField(default=False)


	def __str__(self):
		return self.company_name

	def allow_edit_option(self):
		self.allow_edit = True
		self.save()
	
	def not_allow_edit_option(self):
		self.allow_edit = False
		self.save()

	def update_date(self):
		self.date_of_filling = timezone.now()
		self.save()


class TractionSheet(models.Model):
	connect_startup			      	= models.ForeignKey(StartUp, on_delete=models.CASCADE)
	total_order						= models.CharField(max_length=200,null=True,blank=True)
	average_packet_size				= models.CharField(max_length=200,null=True,blank=True)
	total_revenue_of_month			= models.CharField(max_length=200,null=True,blank=True)
	total_customers_served			= models.CharField(max_length=200,null=True,blank=True)
	total_expense					= models.CharField(max_length=200,null=True,blank=True)
	market_outreach					= models.CharField(max_length=200,null=True,blank=True)
	repeate_customers				= models.CharField(max_length=200,null=True,blank=True)
	total_revenue					= models.CharField(max_length=200,null=True,blank=True)
	direct_job_created				= models.CharField(max_length=200,null=True,blank=True)
	indirect_job_created			= models.CharField(max_length=200,null=True,blank=True)
	profit							= models.CharField(max_length=200,null=True,blank=True)

	allow_edit 						= models.BooleanField(default=False)
	generated_date					= models.DateTimeField(verbose_name='report generated date', auto_now_add=True)


	def __str__(self):
		return self.connect_startup.startup_name

	def allow_edit_option(self):
		self.allow_edit = True
		self.save()

	def not_allow_edit_option(self):
		self.allow_edit = False
		self.save()

	def update_date(self):
		self.generated_date = timezone.now()
		self.save()



class MoM(models.Model):
	from_user 	 				= models.CharField(max_length=100,null=True,blank=True)
	to                          = models.ForeignKey(Account,null=True,blank=True, on_delete=models.CASCADE)
	date_of_creation			= models.DateTimeField(verbose_name='date of creation', auto_now_add=True)
	title						= models.CharField(max_length=500,null=True,blank=True)
	description					= models.CharField(max_length=1000,null=True,blank=True)
	document                    = models.FileField(upload_to='files',null=True,blank=True)

	def __str__(self):
		return self.title	


class BlogPost(models.Model):
	title   					= models.CharField(max_length=1000,null=True,blank=True)
	description			 		= models.CharField(max_length=5000,null=True,blank=True)
	blog_img					= models.ImageField(upload_to='blog_img/',null=True,blank=True)
	date_of_creation			= models.DateTimeField(verbose_name='date of creation', auto_now_add=True)


	def __str__(self):
		return self.title



class WorkGenerator(models.Model):
	from_user					 = models.CharField(max_length=100,null=True,blank=True)
	to                           = models.ForeignKey(Admin,null=True,blank=True, on_delete=models.CASCADE)
	date_of_creation			 = models.DateTimeField(verbose_name='date of creation', auto_now_add=True)	
	title   					 = models.CharField(max_length=1000,null=True,blank=True)
	work_description			 = models.CharField(max_length=2000,null=True,blank=True)
	suggestions					 = models.CharField(max_length=1500,null=True,blank=True)
	remarks						 = models.CharField(max_length=2000,null=True,blank=True)
	status 					 	 = models.CharField(max_length=20,null=True,blank=True)
	document                     = models.FileField(upload_to='files',null=True,blank=True)
	forwarded					 = models.BooleanField(default=False)
	forwarded_from 				 = models.CharField(max_length=200,null=True,blank=True)
	forwarded_to				 = models.CharField(max_length=200,null=True,blank=True)
	date_of_complition			 = models.DateTimeField(blank=True, null=True)
	from_user_pk				 = models.CharField(max_length=500,null=True,blank=True)
	new_work 					 = models.BooleanField(default=True)
	


	def __str__(self):
		return self.title

	def update_work(self,title,work_description,suggestions,remarks):
		self.title = title
		self.work_description = work_description
		self.suggestions = suggestions
		self.remarks = remarks
		self.save()

	def change_status(self,status):
		self.status = status
		self.save()
	def update_date(self):
		self.date_of_complition = timezone.now()
		self.save()
	
	def forward(self,from_user,to):
		self.forwarded = True
		self.forwarded_from = from_user
		self.forwarded_to = to
		self.save()
	
	def make_null(self):
		self.to = None
		self.save()

	def update_to(self,to):
		self.to = to
		self.date_of_creation = timezone.now()
		self.save()
	def remove_forward(self):
		self.forwarded = False
		self.save()

class Forward(models.Model):
	from_user				= models.CharField(max_length=100,null=True,blank=True)
	to  					= models.ForeignKey(Admin,null=True,blank=True, on_delete=models.CASCADE)
	forward_work  			= models.ForeignKey(WorkGenerator,null=True,blank=True,default="", on_delete=models.CASCADE)
	suggestions				= models.CharField(max_length=200,null=True,blank=True)
	forwarded			    = models.BooleanField(default=False)
	date_of_forward			= models.DateTimeField(verbose_name='date of forward', auto_now_add=True,null=True,blank=True)
	from_user_pk		    = models.CharField(max_length=500,null=True,blank=True)
	forward_pk				= models.CharField(max_length=100,null=True,blank=True)
	new_forward		    	= models.BooleanField(default=True)

	def forther_forward(self):
		self.forwarded = True
		self.save()
	def remove_forward(self):
		self.forwarded = False
		self.save()

	def make_null(self):
		self.to = None
		self.save()


	def __str__(self):
		return self.from_user +" " +self.forward_work.title

class Return(models.Model):
	from_user				= models.CharField(max_length=100,null=True,blank=True)
	to  					= models.ForeignKey(Admin, on_delete=models.CASCADE)
	work		  			= models.ForeignKey(WorkGenerator,default="", on_delete=models.CASCADE)
	message				    = models.CharField(max_length=500,null=True,blank=True)
	return_date				= models.DateTimeField(verbose_name='return date', auto_now_add=True,null=True,blank=True)
	forward_pk				= models.CharField(max_length=100,null=True,blank=True)
	new_return		    	= models.BooleanField(default=True)

	def __str__(self):
		return self.from_user

	def assign_forward_pk(self,forward_pk):
		self.forward_pk = forward_pk
		self.save()

	 