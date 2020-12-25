from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_img = models.ImageField(default='images/default.png')
	#dep = models.CharField(max_length=30, blank=False,default='')



@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(profile_user=instance)
	instance.userprofile.save()


statuses = [('accept', 'accept'),
('reject', 'reject'),
('pending', 'pending')
]

class AllLogin(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user.username

class AllLogout(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE)
	date= models.DateTimeField(auto_now_add= True)
    

	def __str__(self):
		return self.user.username

class LeaveApplication(models.Model):
    
    reason = models.CharField(max_length=100 ,blank=False, null=False,default=None )
    status = models.CharField(max_length=20, choices=statuses, default="pending")
    user = models.ForeignKey(User, on_delete= models.CASCADE )
	
	
    def __str__(self):
        return self.user.username



class AppResponse(models.Model):
	leaveapp = models.ForeignKey(LeaveApplication, on_delete=models.CASCADE)
	status = models.CharField(max_length=20, choices=statuses )

	def __str__(self):
		return self.status
