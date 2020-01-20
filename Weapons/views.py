from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.
def Welcome(request):
    return render(request, 'Weapons/Welcome.html')
def Home(request):
    return render(request, 'Weapons/base.html')

def logoutpage(request):
    return render(request,'Weapons/logout.html')
def signup(request):
    form = UserCreationForm(request.POST)
    if request.method=='POST':

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form= UserCreationForm()
    return render(request,'Weapons/registration.html', {'form':form})
@login_required()
def Link(request):
    return render(request,'registration/login.html')



