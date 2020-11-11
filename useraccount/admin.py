from django.contrib import admin
from .models import Account,Admin,StartUp,TeamMembers,MonitorSheet,TractionSheet,WorkGenerator,Forward,Return,MoM,BlogPost,Query
# Register your models here.
admin.site.register(Account)
admin.site.register(Admin)
admin.site.register(StartUp)
admin.site.register(TeamMembers)
admin.site.register(MonitorSheet)
admin.site.register(TractionSheet)
admin.site.register(WorkGenerator)
admin.site.register(Forward)
admin.site.register(Return)
admin.site.register(MoM)
admin.site.register(BlogPost)
admin.site.register(Query)