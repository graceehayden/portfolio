from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone
from .models import *
from .functions import *
from .forms import *
import random


class Portfolio(View):
    def get(self, request):
        return render(request, 'portfolio.html', {})


class Resume(View):
    def get(self, request):
        return render(request, 'resume.html', {})


###########################


def user_signup(request):
    if request.user.is_active:
        return redirect('porfolio')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('portfolio')
        else:
            return render(request, 'user_signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'user_signup.html', {'form': form,
                                                    })

def user_login(request):
    if "login" in request.GET:
        return render(request, 'portfolio.html', {})
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('portfolio')
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "user_login.html",
                  context={"form":form})


    # if request.user.is_active or login == False:
    #     return render(request, 'portfolio.html', {})
    # else:
    #     return redirect('user_login')


def signout(request):
    logout(request)
    return redirect('index')


def inspiration_station(request):
    return render(request, 'coming_soon.html', {})


def function_junction(request):
    return render(request, 'function_junction.html', {})


def palindromes(request):
    answer = ''
    if 'submit' in request.GET:
        answer = check_if_palindrome(request.GET.get('word', ''))

    return render(request, 'function_junction.html', {'answer': answer})


def merge_and_sort_lists(request):
    if 'submit' in request.GET:
        list1 = [random.randrange(1, 50, 1) for i in range(7)]
        list2 = [random.randrange(1, 50, 1) for i in range(7)]
    list = merge_sort_lists(list1, list2)
    return render(request, 'function_junction.html', {'list': list,
                                                      'list1': list1,
                                                      'list2': list2})
