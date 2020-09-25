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
	founders_designation	= models.CharField(max_length=200,null=True,blank=True)
	website					= models.CharField(max_length=100,null=True,blank=True)
	city					= models.CharField(max_length=100,null=True,blank=True)
	sector					= models.CharField(max_length=100,null=True,blank=True)
	team_members			= models.CharField(max_length=100,null=True,blank=True)
	location				= models.CharField(max_length=100,null=True,blank=True)
	contact_no				= models.CharField(max_length=100,null=True,blank=True)

	def __str__(self):
		return self.startup_name
    
    