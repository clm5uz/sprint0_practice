from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User

# Create your views here.
def view_form(request):
	return render(request, 'formtest/form.html', {})

def create_form(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username', '')
			user_obj = User(username = username)
			user_obj.save()
			return HttpResponseRedirect('created_form')
	else:
		form = UserForm()
	return render(request, 'form.html', {
		'form': UserForm(),
	})

def created_form(request):
	return render(request, 'formtest/createdForm.html', {})

