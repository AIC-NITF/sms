from django.contrib import admin
from .models import Account,Admin,StartUp,Founder,TeamMembers
# Register your models here.
admin.site.register(Account)
admin.site.register(Admin)
admin.site.register(StartUp)
admin.site.register(Founder)
admin.site.register(TeamMembers)