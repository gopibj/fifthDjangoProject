
# for Registration
import urllib.request
from django.shortcuts import render, redirect
from basic_app.forms import UserForm, UserProfileInfoForm

# for login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(requset):
    registered = False
    if requset.method == "POST":
        user_form = UserForm(requset.POST)
        profile_form = UserProfileInfoForm(requset.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in requset.FILES:
                profile.profile_pic = requset.FILES['profile_pic']
                    
            profile.save()        
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:    
        user_form = UserForm(requset.POST)
        profile_form = UserProfileInfoForm(requset.POST)
        
    return render(requset, 'basic_app/registration.html',
                                    {'user_form':user_form,
                                    'profile_form':profile_form,
                                    'registered': registered})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("login failed!")
            print("Username:{} and password{}".format(username, password))
            return HttpResponse(" invalid login input supplied!")
    else:
        return render(request, 'basic_app/login.html', {})

@login_required    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("you are logged in!")
    
        

            
            

        