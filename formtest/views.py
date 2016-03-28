from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User
# crytography imports
from Crypto.PublicKey import RSA
from Crypto import Random

# Create your views here.
def view_form(request):
	return render(request, 'formtest/form.html', {})

def create_form(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			# generate key
			random_generator = Random.new().read
			key = RSA.generate(1024, random_generator)
			publicKey = key.publickey()
			# get fields for model
			username = request.POST.get('username', '')
			pwd = request.POST.get('password', '')
			user_obj = User(username = username, password = pwd, public_key = publicKey)
			user_obj.save()
			return HttpResponseRedirect('created_form')
	else:
		form = UserForm()
	return render(request, 'form.html', {
		'form': UserForm(),
	})

def created_form(request):
	return render(request, 'formtest/createdForm.html', {})

