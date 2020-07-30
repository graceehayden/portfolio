from django.shortcuts import render, render_to_response, redirect
from django.contrib import messages
from django.utils import timezone
from django.template import RequestContext
import random


def home(request):
    ''' Home page '''
    return render(request, 'home.html', {})


def inspiration_station(request):
    return render(request, 'home.html', {})


def travel_inspiration(request):
    return render(request, 'travel_inspiration.html', {})


def post_list(request):
    posts = Post.objects.order_by('published_date')[:3]
    return render(request, 'function_junction.html', {'posts': posts})


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


def hello_pallet(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'hello_pallet.html', {'posts': posts})
