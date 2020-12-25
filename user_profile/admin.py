from django.contrib import admin
from user_profile.models import UserProfile, LeaveApplication,AppResponse, AllLogin, AllLogout
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(LeaveApplication)
admin.site.register(AppResponse)
admin.site.register(AllLogin)
admin.site.register(AllLogout)



