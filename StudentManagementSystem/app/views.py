from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser



def BASE(request):

	return render(request,'base.html')


def LOGIN(request):
	return render(request,'login.html')


def doLogout(request):
	logout(request)
	return redirect('login')

def doLogin(request):
	if request.method == 'POST':
		user = EmailBackEnd.authenticate(request,username=request.POST.get('email'), password = request.POST.get('password'),)
		print("--------user---")
		print(user)
		if user!=None:
			login(request,user)
			user_type = user.user_type
			if user_type =='HOD':
				return redirect('hodhome')

			elif user_type =='TEACHER':
				return redirect('teacherhome')

			elif user_type =='STUDENT':
				return redirect('studenthome')

			else:
				messages.error(request,"Email and Password are Incorrect !")
				return redirect ('login')
		else:
			messages.error(request,"Email and Password are Incorrect")
			return redirect('login')

	else:
		return redirect('login')

@login_required(login_url='login')
def profile(request):
	user = CustomUser.objects.get(id= request.user.id)
	print('--------------------------')
	print(user)

	return render(request,'profile.html',{'user':user})

@login_required(login_url='login')
def profile_update(request):
	if request.method =='POST':
		password = request.POST.get('password')
		print('----------')
		print(password)
		profile_pic = request.FILES.get('profile_pic')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		print(password)

		try:
			customuser = CustomUser.objects.get(id = request.user.id)
			customuser.first_name = first_name
			customuser.last_name = last_name
			print(password)
			if profile_pic  != None and profile_pic != '':
				customuser.profile_pic = profile_pic
			if password  != None and password != '':
				customuser.set_password(password)
			customuser.save()
			messages.success(request,'Profile is updated !')
			return redirect('profile')

		except :
			messages.error(request,'Profile Update Failed !')
			return redirect('profile')
			

	else:
		return render(request,'profile.html')