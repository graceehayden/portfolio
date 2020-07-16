from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import Post
from django.template import RequestContext
from .functions import *
import random
from .models import *
from .forms import *


def coming_soon(request):
    return render(request, 'coming_soon.html', {})


def resume(request):
    return render(request, 'resume.html', {})


def portfolio(request):
    return render(request, 'portfolio.html', {})


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
    videos = []
    videos = Video.objects.all()

    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context= {
              'videos': videos,
              'form': form
              }

    return render(request, 'videos.html', context)


def hello_pallet(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'hello_pallet.html', {'posts': posts})


def error(request):
    return render(request, 'error.html', {})


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
