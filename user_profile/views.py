
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import UserProfile, LeaveApplication, AllLogin,AllLogout
from django.conf import settings
import os
from .forms import RegisterForm, SigninForm,LeaveForm


def home(request):
	return render(request, 'user_profile/home.html')



def user_signup(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")	
		try:
			user_obj = User.objects.create(username=username, email=email)
			user_obj.is_active = False
			user_obj.set_password(password)
			user_obj.save()
			#user_auth = authenticate(username=username, password=userpass)
			#login(request, user_auth)
			return redirect('home')
		except:
			messages.add_message(request, messages.ERROR, 'Unable to sign up.')
			return render(request, 'user_profile/signup.html')
	return render(request, 'user_profile/signup.html', {'form': form})
		





def user_login(request):
	form = SigninForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user!=1 :

			login(request, user)
			AllLogin.objects.create(user= request.user)
			return redirect("home")
		else:
			request.session['invalid_error'] = 1

	return render(request, 'user_profile/login.html', {'form': form})


def user_logout(request):
	try:
		logout(request)
		AllLogout.objects.create(user=request.user)
		
		messages.add_message(request, messages.INFO, 'You\'re logged Out!')
	except:
		messages.add_message(request, messages.ERROR, "Unable to log out.")
	return redirect('home')


@login_required
def user_profile(request, user_id):

	if request.method == 'POST':
		user_obj = User.objects.get(id=user_id)
		user_profile_obj = UserProfile.objects.get(id=user_id)
		
		user_img = request.FILES['user_img']
		fs_handle = FileSystemStorage()
		img_name = 'images/user_{0}'.format(user_id)
		if fs_handle.exists(img_name):
			fs_handle.delete(img_name)
		fs_handle.save(img_name, user_img)
		user_profile_obj.profile_img = img_name
		user_profile_obj.save()
		user_profile_obj.refresh_from_db()
		
		return render(request, 'user_profile/my_profile.html', {'my_profile': user_profile_obj})
	if (request.user.is_authenticated and request.user.id == user_id):
		user_obj = User.objects.get(id=user_id)
		user_profile = UserProfile.objects.get(id=user_id)

		return render(request, 'user_profile/my_profile.html', {'my_profile': user_profile})




def LeaveApp(request):
	form = LeaveForm(request.POST or None )
	emp = User.objects.filter(username=request.user).first()
	if form.is_valid():
		form.instance.user =emp
		form.save()
		
		
	
	context = {'form': form}
	
	return render(request, 'user_profile/leavingApp.html', context)
	

	

		

def ShowResp(request):
	emp = User.objects.filter(username=request.user).first()
	app = LeaveApplication.objects.filter(user=emp).all()

	context = { 'app':app }
	return render(request,'user_profile/showresp.html',context)






