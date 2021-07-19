from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth



def signin_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password1']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, ("there was an error try again"))
			return redirect("signin")
	else:
		return render(request,'authenticate/signin.html', {})



def signup_user(request):

	
	if request.method == "POST":

		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password2==password1:
			if User.objects.filter(username=username).exists():
				messages.info(request, ("Username already exists"))
				return redirect("signup")
			elif User.objects.filter(email=email).exists():
				messages.info(request, ("Email already exists"))
				return redirect("signup")
			else:
				user = User.objects.create_user(username=username, email=email, password=password2)
				user.save();
				messages.info(request, ("Successfully user created"))
				return redirect('home')
		else:
			messages.info(request, ("Password does not match"))
			return redirect("signup")


	else:
		return render(request, 'authenticate/signup.html', {})


def signout_user(request):
		logout(request)
		return redirect('home')

