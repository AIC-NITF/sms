from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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

	def __str__(self):
		return self.startup_name
    

class Founder(models.Model):
	startup  				= models.ForeignKey(StartUp, on_delete=models.CASCADE)
	name 					= models.CharField(max_length=100,null=True,blank=True)
	gender 					= models.CharField(max_length=10,null=True,blank=True)
	email 					= models.CharField(max_length=100,null=True,blank=True)
	contact_no 				= models.CharField(max_length=200,null=True,blank=True)


	def __str__(self):
		return self.name

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
	date_of_filling					= models.CharField(max_length=200,null=True,blank=True)
	
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


	def __str__(self):
		return self.company_name +" " +self.date_of_filling

