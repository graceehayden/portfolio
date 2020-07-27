from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.template import RequestContext
from .models import Post
from .functions import *
from .models import *
from .forms import *
import random


def index(request):
    return render(request, 'index.html', {})


def coming_soon(request):
    return render(request, 'coming_soon.html', {})


def resume(request):
    return render(request, 'resume.html', {})


def portfolio(request):
    return render(request, 'portfolio.html', {})


def travel_inspiration(request):
    return render(request, 'travel_inspiration.html', {})


def inspiration_station(request):
    return render(request, 'inspiration_station.html', {})


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

    #if 'submit' in request.POST:
    #    name = request.POST('name')
    #    videofile = request.POST('videofile')

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
