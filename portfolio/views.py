from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone
from django.template import RequestContext
from .models import *
from .functions import *
from .forms import *
import random


def index(request):
    ''' Home page '''
    return render(request, 'index.html', {})


def user_signup(request):
    if request.user.is_active:
        return redirect('index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'user_signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'user_signup.html', {'form': form,
                                                    })


def user_login(request):
    # redirect_view = str(request.POST.get('redirect_view'))
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect(index)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "user_login.html",
                    context={"form":form})


def signout(request):
    logout(request)
    return redirect('index')


def coming_soon(request):
    return render(request, 'coming_soon.html', {})


def resume(request):
    return render(request, 'resume.html', {})


def portfolio(request):
    if request.user.is_active:
        return render(request, 'portfolio.html', {})
    else:
        return redirect('user_login')


def inspiration_station(request):
    return render(request, 'coming_soon.html', {})


def travel_inspiration(request):
    return render(request, 'travel_inspiration.html', {})


def function_junction(request):
    return render(request, 'function_junction.html', {})


def palindromes(request):
    answer = ''
    if 'submit' in request.GET:
        answer = check_if_palindrome(request.GET.get('word', ''))

    return render(request, 'function_junction.html', {'answer': answer})


def post_list(request):
    posts = Post.objects.order_by('published_date')[:3]
    return render(request, 'function_junction.html', {'posts': posts})


def merge_and_sort_lists(request):
    if 'submit' in request.GET:
        list1 = [random.randrange(1, 50, 1) for i in range(7)]
        list2 = [random.randrange(1, 50, 1) for i in range(7)]
    list = merge_sort_lists(list1, list2)
    return render(request, 'function_junction.html', {'list': list,
                                                      'list1': list1,
                                                      'list2': list2})


def videos(request):
    request.session['page'] = 'videos'
    if not request.user.is_active:
        return redirect('user_login')
    else:
        form= VideoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        videos = []
        videos = Video.objects.all()
        print(videos)
        context= {
                  'videos': videos,
                  'form': form
                  }
        return render(request, 'videos.html', context)



def error(request):
    return render(request, 'error.html', {})

#def hello_pallet(request):
#    posts = Post.objects.order_by('published_date')
#    return render(request, 'hello_pallet.html', {'posts': posts})


#def handler404(request, *args, **argv):
#    response = render_to_response('error.html', {},
#                                  context_instance=RequestContext(request))
#    response.status_code = 404
#    return response


# def handler500(request, *args, **argv):
#    response = render_to_response('error.html', {},
#                                  context_instance=RequestContext(request))
#    response.status_code = 500
#    return response
