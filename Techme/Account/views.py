from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from django.shortcuts import render

# Create your views here.

#function for render form html page 
def register(request):
    return render(request,'Account/register.html')

def logins(request):
    if request.method=="POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request,'Account/login.html')


def logouts(request):
    logout(request)
    return redirect('login')
