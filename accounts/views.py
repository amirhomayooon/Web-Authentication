from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render

from .forms import LoginForm, UserRegistrationForm, UserEditForm
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                    username=cd['username'],
                    password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Done, Welcome')
                else:
                    return HttpResponse('Disabled Account')
        else:
            return('Login Invalid')
    else:
        form = LoginForm()
    return render(request,
    'accounts/login.html',
    {'form' : form})
        
@login_required
def mainpage(request):
    return render(request,
    'accounts/mainpage.html',
    {'section' : 'mainpage'})

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
            'accounts/register_done.html', 
            {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
    'accounts/register.html',
    {'user_form':user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile Updated Successfully')
        else:
            messages.error(request, 'Error Updating Your Profile')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request,
    'accounts/edit.html',
    {'user_form':user_form})
