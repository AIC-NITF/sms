from django.contrib import admin
from .models import Account,Admin,StartUp,TeamMembers,WorkGenerator,Forward,Return,MoM,BlogPost,Query,Gallery,LeaveApplication,Attendence,EmpMessage,MonitorSheetReport
# Register your models here.
admin.site.register(Account)
admin.site.register(Admin)
admin.site.register(StartUp)
admin.site.register(TeamMembers)
admin.site.register(MonitorSheetReport)
admin.site.register(WorkGenerator)
admin.site.register(Forward)
admin.site.register(Return)
admin.site.register(MoM)
admin.site.register(BlogPost)
admin.site.register(Query)
admin.site.register(Gallery)
admin.site.register(LeaveApplication)
admin.site.register(Attendence)
admin.site.register(EmpMessage)